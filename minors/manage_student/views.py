from operator import itemgetter

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.shortcuts import render_to_response, redirect

from utbroker.errors import UTBrokerError
from utdirect.templates import UTDirectContext

from degree.minors.manage_student.utd_defaults import PROJECT_UTD_DEFAULTS, PROJECT_UTD_DEFAULTS_ADMIN
from degree.minors.utils.csv_export import convert_dicts_to_CSV_response
from degree.minors.manage_student.nrdpscrr import Nrdpscrr
from degree.minors.manage_student.nrdpscrc import Nrdpscrc
from degree.minors.manage_student.nrdpscru import Nrdpscru
from degree.minors.manage_student.nrdpscrl import Nrdpscrl
from degree.minors.manage_student.nrdpscrv import Nrdpscrv

DEFAULT_SORT_DIRECTION = 'A'

def search_by_eid(request):

    context = {}
    results = []
    submit = True
    form_submitted = False
    defaults = PROJECT_UTD_DEFAULTS

    if 'eid_submitted' in request.GET:
        nrdpscrv = Nrdpscrv()
        nrdpscrv.send.webtoken = request.META['HTTP_TOKEN']
        nrdpscrv.send.form_submitted = 'X'
        nrdpscrv.send.code_or_eid_submitted = 'X'
        nrdpscrv.send.code_or_eid_input = 'E' + request.GET.get('eid_report')

        try:
            nrdpscrv.call_broker_once(service=request.META['HTTP_SERVICE'])

        except (UTBrokerError), error_info:
            error_msg = str(error_info)
            return render_to_response('error.html', UTDirectContext(request,
                                                                    {'error_msg': error_msg},
                                                                    defaults=defaults,
                                                                    document_title='Broker Error', ))

        context['nrdpscrv.recv'] = nrdpscrv.recv
        context['nrdpscrv.send'] = nrdpscrv.send
        context['job_number'] = nrdpscrv.recv.job_numbers[0]

        if nrdpscrv.send.form_submitted and not nrdpscrv.recv.return_code:
            messages.success(request, "The report has been successfully submitted.")

    nrdpscrr = Nrdpscrr()
    nrdpscrr.send.webtoken = request.META['HTTP_TOKEN']

    if 'eid_submitted' in request.GET:
        nrdpscrr.send.eid = request.GET.get('eid_report')
    else:
        nrdpscrr.send.eid = request.GET.get('s_eid', '')

    if 'submit' in request.GET or 'next_page_submitted' in request.GET or 'eid_submitted' in request.GET:
        form_submitted = True
        nrdpscrr.send.form_submitted = 'X'

    if request.GET.get('sort_direction') == None:
        sort_direction = DEFAULT_SORT_DIRECTION
    else:
        sort_direction = request.GET.get('sort_direction')

    if sort_direction == 'A':
        next_sort_direction = 'D'
    else:
        next_sort_direction = 'A'

    while submit == True:
        nrdpscrr.send.paging_isn = nrdpscrr.recv.paging_isn
        nrdpscrr.send.paging_data_source = nrdpscrr.recv.paging_data_source

        try:
            nrdpscrr.call_broker_once(service=request.META['HTTP_SERVICE'])

        except (UTBrokerError), error_info:

            error_msg = str(error_info)
            return render_to_response('error.html', UTDirectContext(request,
                {'error_msg': error_msg},
                defaults=defaults,
                document_title = 'Broker Error',))

        for item in nrdpscrr.recv.recs_returned:
            catalog = ''
            conferred_ccyys = ''
            if item.catalog_beg != '0':
                catalog = item.catalog_beg[0:4] + '-' + item.catalog_end[0:4]
            if item.conferred_ccyys != '0':
                conferred_ccyys = item.conferred_ccyys
            if item.doc_nbr:
                results.append({'eid': item.eid,
                                'name': item.name,
                                'doc_nbr': item.doc_nbr,
                                'type': item.type,
                                'status': item.status,
                                'credential_code': item.credential_code,
                                'credential_desc_long': item.credential_desc_long,
                                'pursuing': item.pursuing,
                                'effective_ccyys': item.effective_ccyys,
                                'catalog': catalog,
                                'catalog_beg': item.catalog_beg,
                                'catalog_end': item.catalog_end,
                                'conferred_ccyys': conferred_ccyys,
                                })

        if not nrdpscrr.recv.paging_isn:
            submit = False

        if 'csv' in request.GET.get('export', ''):
            return inbox_download(results)

        if nrdpscrr.recv.is_reg_admin == 'X':
            defaults = PROJECT_UTD_DEFAULTS_ADMIN

    sort_key =  str(request.GET.get('sort', '')) or 'status'
    results = sorted(results, key=itemgetter(sort_key))

    if sort_direction == 'D':
        results.reverse()

    paginator = Paginator(results, 25)

    page = request.GET.get('page')

    try:
        credentials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        credentials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        credentials = paginator.page(paginator.num_pages)

    context['credentials'] = credentials
    context['recv'] = nrdpscrr.recv
    context['send'] = nrdpscrr.send
    context['form_submitted'] = form_submitted
    context['sort_direction'] = sort_direction
    context['next_sort_direction'] = next_sort_direction
    context['sort_key'] = sort_key
    context['this_url'] = request.get_full_path()

    print 'hey', request.GET.get('eid')
    print request.get_full_path()




    return render_to_response("search_by_eid.html", UTDirectContext(request, context, defaults=defaults))

def search_by_code(request):

    defaults = PROJECT_UTD_DEFAULTS
    context = {}
    results = []
    submit = True
    form_submitted = False
    nrdpscrc = Nrdpscrc()

    if 'code_submitted' in request.GET:
        nrdpscrv = Nrdpscrv()
        nrdpscrv.send.webtoken = request.META['HTTP_TOKEN']
        nrdpscrv.send.form_submitted = 'X'
        nrdpscrv.send.code_or_eid_submitted = 'X'
        nrdpscrv.send.code_or_eid_input = 'C' + request.GET.get('code')

        try:
            nrdpscrv.call_broker_once(service=request.META['HTTP_SERVICE'])

        except (UTBrokerError), error_info:
            error_msg = str(error_info)
            return render_to_response('error.html', UTDirectContext(request,
                                                                    {'error_msg': error_msg},
                                                                    defaults=defaults,
                                                                    document_title='Broker Error', ))

        context['nrdpscrv.recv'] = nrdpscrv.recv
        context['nrdpscrv.send'] = nrdpscrv.send
        context['job_number'] = nrdpscrv.recv.job_numbers[0]

        if nrdpscrv.send.form_submitted and not nrdpscrv.recv.return_code:
            messages.success(request, "The report has been successfully submitted.")

    if 'submit' in request.GET or 'code_submitted' in request.GET:
        form_submitted = True
        nrdpscrc.send.form_submitted = 'X'

    if request.GET.get('sort_direction') == None:
        sort_direction = DEFAULT_SORT_DIRECTION
    else:
        sort_direction = request.GET.get('sort_direction')

    if sort_direction == 'A':
        next_sort_direction = 'D'
    else:
        next_sort_direction = 'A'

    nrdpscrc.send.webtoken = request.META['HTTP_TOKEN']
    if 'code_submitted' in request.GET:
        nrdpscrc.send.credential_code = request.GET.get('code', '')
        nrdpscrc.send.status = request.GET.get('status_report', '')
    else:
        nrdpscrc.send.credential_code = request.GET.get('s_credential_code', '')
        nrdpscrc.send.status = request.GET.get('s_status', '')

    while submit:
        try:
            nrdpscrc.call_broker_once(service=request.META['HTTP_SERVICE'])

        except (UTBrokerError), error_info:

            error_msg = str(error_info)
            return render_to_response('error.html', UTDirectContext(request,
                                                                    {'error_msg': error_msg},
                                                                    defaults=defaults,
                                                                    document_title='Broker Error', ))

        for item in nrdpscrc.recv.recs_returned:
            if item.doc_nbr:
                catalog = ''
                conferred_ccyys = ''
                if item.catalog_beg != '0':
                    catalog = item.catalog_beg[0:4] + '-' + item.catalog_end[0:4]
                if item.conferred_ccyys != '0':
                    conferred_ccyys = item.conferred_ccyys
                results.append({'eid': item.eid,
                                'name': item.name,
                                'doc_nbr': item.doc_nbr,
                                'type': item.type,
                                'status': item.status,
                                'credential_code': nrdpscrc.recv.credential_code,
                                'credential_desc_long': nrdpscrc.recv.credential_desc_long,
                                'pursuing': item.pursuing,
                                'effective_ccyys': item.effective_ccyys,
                                'catalog': catalog,
                                'conferred_ccyys': conferred_ccyys,
                                })


        if not nrdpscrc.recv.paging_isn:
            submit = False
        if 'csv' in request.GET.get('export', ''):
            return inbox_download(results)

        nrdpscrc.send.paging_isn = nrdpscrc.recv.paging_isn
        nrdpscrc.send.paging_time = nrdpscrc.recv.paging_time
        nrdpscrc.send.paging_effective_ccyys = nrdpscrc.recv.paging_effective_ccyys

    if nrdpscrc.recv.is_reg_admin == 'X':
        defaults = PROJECT_UTD_DEFAULTS_ADMIN

    sort_key = str(request.GET.get('sort', '')) or 'eid'
    results = sorted(results, key=itemgetter(sort_key))

    if sort_direction == 'D':
        results.reverse()

    paginator = Paginator(results, 25)

    page = request.GET.get('page')

    try:
        credentials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        credentials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        credentials = paginator.page(paginator.num_pages)



    context['credentials'] = credentials
    context['recv'] = nrdpscrc.recv
    context['send'] = nrdpscrc.send
    context['form_submitted'] = form_submitted
    context['sort_direction'] = sort_direction
    context['next_sort_direction'] = next_sort_direction
    context['sort_key'] = sort_key
    context['this_url'] = request.get_full_path()

    return render_to_response("search_by_code.html", UTDirectContext(request, context, defaults=defaults))

def late_add_inbox(request):
    defaults = PROJECT_UTD_DEFAULTS
    context = {}
    results = []
    submit = True
    form_submitted = False
    nrdpscrl = Nrdpscrl()

    if request.GET.get('sort_direction') == None:
        sort_direction = DEFAULT_SORT_DIRECTION
    else:
        sort_direction = request.GET.get('sort_direction')

    if sort_direction == 'A':
        next_sort_direction = 'D'
    else:
        next_sort_direction = 'A'

    nrdpscrl.send.webtoken = request.META['HTTP_TOKEN']

    while submit:
        try:
            nrdpscrl.call_broker_once(service=request.META['HTTP_SERVICE'])

        except (UTBrokerError), error_info:

            error_msg = str(error_info)
            return render_to_response('error.html', UTDirectContext(request,
                                                                    {'error_msg': error_msg},
                                                                    defaults=defaults,
                                                                    document_title='Broker Error', ))

        for item in nrdpscrl.recv.recs_returned:

            if item.doc_nbr:
                print item.credential_desc_long
                catalog = ''
                conferred_ccyys = ''
                if item.catalog_beg != '0':
                    catalog = item.catalog_beg[0:4] + '-' + item.catalog_end[0:4]
                if item.conferred_ccyys != '0':
                    conferred_ccyys = item.conferred_ccyys
                results.append({'eid': item.eid,
                                'name': item.name,
                                'type': item.type,
                                'doc_nbr': item.doc_nbr,
                                'status': item.status,
                                'credential_code': item.credential_code,
                                'credential_desc_long': item.credential_desc_long,
                                'pursuing': item.pursuing,
                                'effective_ccyys': item.effective_ccyys,
                                'catalog': catalog,
                                'conferred_ccyys': conferred_ccyys,
                                })


        if not nrdpscrl.recv.paging_isn:
            submit = False

        if 'csv' in request.GET.get('export', ''):
            return inbox_download(results)

        nrdpscrl.send.paging_isn = nrdpscrl.recv.paging_isn
        # nrdpscrl.send.paging_time = nrdpscrl.recv.paging_time

    if nrdpscrl.recv.is_reg_admin == 'X':
        defaults = PROJECT_UTD_DEFAULTS_ADMIN

    sort_key = str(request.GET.get('sort', '')) or 'eid'
    results = sorted(results, key=itemgetter(sort_key))

    if sort_direction == 'D':
        results.reverse()

    paginator = Paginator(results, 25)

    page = request.GET.get('page')

    try:
        credentials = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        credentials = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        credentials = paginator.page(paginator.num_pages)

    context['credentials'] = credentials
    context['recv'] = nrdpscrl.recv
    context['send'] = nrdpscrl.send
    context['form_submitted'] = form_submitted
    context['sort_direction'] = sort_direction
    context['next_sort_direction'] = next_sort_direction
    context['sort_key'] = sort_key
    context['this_url'] = request.get_full_path()


    return render_to_response("late_add_inbox.html", UTDirectContext(request, context, defaults=defaults))

def inbox_download(student_credentials):
    """Creates a csv download of the student major records provided. Assumes that
    the last update info is attached to queryset as an annotation."""

    field_keys = ['eid', 'name', 'type', 'status', 'credential_code', 'credential_desc_long', 'pursuing',
                  'effective_ccyys', 'catalog', 'conferred_ccyys']
    csv_title = 'credentials'
    field_display_titles = ['EID', 'Name', 'Type', 'Status', 'Credential Code', 'Credential Description', 'Pursuing',
                            'Effective CCYYS', 'Catalog', 'Degree CCYYS']
    response = convert_dicts_to_CSV_response(student_credentials, field_keys, csv_title,
                                             header_msg=None, field_display_titles=field_display_titles)
    return response

def student_credential(request, doc_nbr=''):

    defaults = PROJECT_UTD_DEFAULTS
    context = {}

    form_submitted = False
    nrdpscru = Nrdpscru()
    nrdpscru.send.webtoken = request.META['HTTP_TOKEN']
    nrdpscru.send.doc_nbr = doc_nbr
    display_as_static = False

    if 'submit' in request.POST:

        form_submitted = True

        if request.POST.get('catalog_beg_ccyy', 0):
            nrdpscru.send.catalog_beg_ccyy = request.POST.get('catalog_beg_ccyy', 0)
            nrdpscru.send.catalog_beg_s = '9'
        else:
            nrdpscru.send.catalog_beg_ccyy = '0'
            nrdpscru.send.catalog_beg_s = '0'
        nrdpscru.send.catalog_end = request.POST.get('catalog_end', 0)
        if request.POST.get('effective_ccyys', 0):
            nrdpscru.send.effective_ccyys = request.POST.get('effective_ccyys', 0)
        else:
            nrdpscru.send.effective_ccyys = 0
        if request.POST.get('coursework_satisfied_ccyys'):
            nrdpscru.send.coursework_satisfied_ccyys = request.POST.get('coursework_satisfied_ccyys', 0)
        else:
            nrdpscru.send.coursework_satisfied_ccyys = 0
        if request.POST.get('conferred_ccyys'):
            nrdpscru.send.conferred_ccyys = request.POST.get('conferred_ccyys', 0)
        else:
            nrdpscru.send.conferred_ccyys = 0
        nrdpscru.send.status = request.POST.get('status', '')
        nrdpscru.send.comments = request.POST.get('comments', '').encode('ascii', 'ignore')
        nrdpscru.send.update = 'Y'

    try:
        nrdpscru.call_broker_once(service=request.META['HTTP_SERVICE'])

    except (UTBrokerError), error_info:
        error_msg = str(error_info)
        return render_to_response('error.html', UTDirectContext(request,
            {'error_msg': error_msg},
            defaults=defaults,
            document_title = 'Broker Error',))

    if nrdpscru.recv.is_reg_admin == 'X':
        defaults = PROJECT_UTD_DEFAULTS_ADMIN
    if nrdpscru.recv.status == 'E':
        display_as_static = True
    if nrdpscru.recv.status == 'C' and not nrdpscru.recv.is_reg_admin:
        display_as_static = True

    context['doc_nbr'] = doc_nbr
    context['recv'] = nrdpscru.recv
    context['send'] = nrdpscru.send
    context['effective_ccyys'] = nrdpscru.recv.effective_ccyys
    context['status'] = nrdpscru.recv.status
    context['catalog_beg_ccyy'] = nrdpscru.recv.catalog_beg_ccyy
    context['coursework_satisfied_ccyys'] = nrdpscru.recv.coursework_satisfied_ccyys
    context['conferred_ccyys'] = nrdpscru.recv.conferred_ccyys
    context['comment_array'] = []

    for item in nrdpscru.recv.comment_array:
        if item.comments:
            context['comment_array'].append(item)

    context['degree_array'] = []

    for item in nrdpscru.recv.degree_array:
        if item.degree:
            print item.degree_ccyys
            context['degree_array'].append(item)

    context['form_submitted'] = form_submitted
    context['display_as_static'] = display_as_static

    if nrdpscru.recv.return_code:
        context['effective_ccyys'] = nrdpscru.send.effective_ccyys
        context['status'] = nrdpscru.send.status
        context['catalog_beg_ccyy'] = nrdpscru.send.catalog_beg_ccyy
        context['coursework_satisfied_ccyys'] = nrdpscru.send.coursework_satisfied_ccyys
        context['conferred_ccyys'] = nrdpscru.send.conferred_ccyys

    if 'submit' in request.POST and not nrdpscru.recv.return_code:
        messages.success(request, "The record has been successfully updated.")
        return redirect('credential_by_doc_nbr', doc_nbr=doc_nbr)

    return render_to_response("student_credential.html", UTDirectContext(request, context, defaults=defaults))



def reports(request):

    defaults = PROJECT_UTD_DEFAULTS
    context = {}

    nrdpscrv = Nrdpscrv()
    nrdpscrv.send.webtoken = request.META['HTTP_TOKEN']

    if 'counts_submitted' in request.GET \
    or 'code_submitted' in request.GET  \
    or 'eid_submitted' in request.GET:
        nrdpscrv.send.form_submitted = 'X'

    if 'counts_submitted' in request.GET:
        nrdpscrv.send.counts_submitted = 'X'

    if 'code_submitted' in request.GET:
        nrdpscrv.send.code_or_eid_submitted = 'X'
        nrdpscrv.send.code_or_eid_input = 'C' + request.GET.get('code')

    if 'eid_submitted' in request.GET:
        nrdpscrv.send.code_or_eid_submitted = 'X'
        nrdpscrv.send.code_or_eid_input = 'E' + request.GET.get('eid')

    try:
        nrdpscrv.call_broker_once(service=request.META['HTTP_SERVICE'])

    except (UTBrokerError), error_info:
        error_msg = str(error_info)
        return render_to_response('error.html', UTDirectContext(request,
                                                                {'error_msg': error_msg},
                                                                defaults=defaults,
                                                                document_title='Broker Error', ))

    if nrdpscrv.recv.is_reg_admin == 'X':
        defaults = PROJECT_UTD_DEFAULTS_ADMIN

    context['recv'] = nrdpscrv.recv
    context['send'] = nrdpscrv.send
    context['job_number'] = nrdpscrv.recv.job_numbers[0]

    if nrdpscrv.send.form_submitted and not nrdpscrv.recv.return_code:
        messages.success(request, "The report has been successfully submitted.")

    return render_to_response("reports.html", UTDirectContext(request, context, defaults=defaults))





