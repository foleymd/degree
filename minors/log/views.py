from datetime import datetime
import logging
import re

from django.contrib import messages
from django.shortcuts import render_to_response, redirect

from utbroker.errors import UTBrokerError
from utdirect.templates import UTDirectContext

from degree.minors.utils.constants import STATUS
from degree.minors.common.utd_defaults import PROJECT_UTD_DEFAULTS
from degree.minors.log.nrdpsclg import Nrdpsclg


def search(request):
    """Allows searching by EID of student."""

    context = {}
    defaults = PROJECT_UTD_DEFAULTS
    error = False

    nrdpsclg = Nrdpsclg()
    nrdpsclg.send.webtoken = request.META['HTTP_TOKEN']
    try:

        nrdpsclg.call_broker_once(service=request.META['HTTP_SERVICE'])
    except UTBrokerError as err:
        messages.error(request, err)
        error = True

    if nrdpsclg.recv.return_code:
        logging.error('User: {0} - {1} ({2})'.format(request.META['HTTP_UTLOGIN_EID'],
                                                     nrdpsclg.recv.return_msg,
                                                     nrdpsclg.recv.return_code))
        messages.error(request, nrdpsclg.recv.return_msg)
        error = True
    if error:
        return render_to_response('log.html', UTDirectContext(request,
                                                              context,
                                                              defaults=defaults,
                                                              document_title='Error',))

    if request.GET.get('search_eid', False):
        eid = re.match(r'^\w{3,8}', request.GET['search_eid'])
        if not eid:
            messages.error(request, "Invalid EID entered.")
        else:
            return redirect('logs_by_eid', eid=request.GET['search_eid'])

    context['recv'] = nrdpsclg.recv
    context['send'] = nrdpsclg.send

    return render_to_response("log.html",
                          UTDirectContext(request, context, defaults=defaults))


def logs_by_eid(request, eid=""):
    """Returns all records related to a given EID."""

    context = {}
    defaults = PROJECT_UTD_DEFAULTS
    error = False

    nrdpsclg = Nrdpsclg()
    nrdpsclg.send.webtoken = request.META['HTTP_TOKEN']
    nrdpsclg.send.search_eid = eid.encode('ascii', 'ignore')
    nrdpsclg.send.paging_isn = request.GET.get('paging_isn', 0)
    nrdpsclg.send.paging_create_date_cymd = request.GET.get('paging_create_date_cymd', 0)
    nrdpsclg.send.paging_create_time = request.GET.get('paging_create_time', 0)

    try:
        nrdpsclg.call_broker_once(service=request.META['HTTP_SERVICE'])
    except UTBrokerError as err:
        messages.error(request, err)
        error = True

    if nrdpsclg.recv.return_code:
        logging.error('User: {0} - {1} ({2})'.format(request.META['HTTP_UTLOGIN_EID'],
                                                     nrdpsclg.recv.return_msg,
                                                     nrdpsclg.recv.return_code))
        messages.error(request, nrdpsclg.recv.return_msg)
        error = True
    if error:
        return render_to_response('log.html', UTDirectContext(request,
                                                              context,
                                                              defaults=defaults,
                                                              document_title='Error',))

    logs = []
    for log in nrdpsclg.recv.recs_returned:
        if log.doc_nbr:
            if log.log_code == 'USTAT' or log.log_code == 'UCMST':
                log.old_value = STATUS.get(log.old_value, '')
                log.new_value = STATUS.get(log.new_value, '')
            logs.append({'log_desc': log.log_desc,
                         'credential_code': log.credential_code,
                         'old_value': log.old_value,
                         'new_value': log.new_value,
                         'create_id': log.create_id,
                         'create_date_display': datetime.strptime(str(log.create_date_cymd), '%Y%m%d').strftime("%m/%d/%Y"),
                         'create_time_display': datetime.strptime(str(log.create_time).zfill(7)[0:6], '%H%M%S').strftime("%I:%M %p"),
                        })
    context['recv'] = nrdpsclg.recv
    context['send'] = nrdpsclg.send
    context['logs'] = logs

    document_title = 'Logs for {0}'.format(eid)

    return render_to_response("log.html",
                              UTDirectContext(request, context, defaults=defaults,
                                              document_title=document_title))