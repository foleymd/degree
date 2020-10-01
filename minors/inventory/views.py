from django.shortcuts import render_to_response
from django.utils.datastructures import OrderedDict

from utbroker.errors import UTBrokerError
from utdirect.templates import UTDirectContext

# from degree.minors.settings import STATIC_URL
from django.conf import settings
from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS_AUTH
from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS
from degree.minors.inventory.nrdpmnmp import Nrdpmnmp


# *************************************************************************** #
#                  Main Function                                                                                    
# *************************************************************************** #

def index(request):                             
    nrdpmnmp = Nrdpmnmp()

    nrdpmnmp.send.webtoken = request.META['HTTP_TOKEN']      
 
    if request.GET.get('page_status', '') != '':
        nrdpmnmp.send.status = request.GET.get('page_status', '')
    else:
        nrdpmnmp.send.status = request.GET.get('search_status', '')
 
    if request.GET.get('page_minor_type', '') != '':
        nrdpmnmp.send.minor_type = request.GET.get('page_minor_type', '')
    else:
        nrdpmnmp.send.minor_type = request.GET.get('search_minor_type', '')
 
    if request.GET.get('page_school', '') != '':
        nrdpmnmp.send.school = request.GET.get('page_school', '')
    else:
        nrdpmnmp.send.school = request.GET.get('search_school', '')
    
    if request.GET.get('page_field_of_study', '') != '':
        nrdpmnmp.send.field_of_study = request.GET.get('page_field_of_study', '')
    else:
        nrdpmnmp.send.field_of_study = request.GET.get('search_field_of_study', '')
 
    nrdpmnmp.send.search_status = request.GET.get('s_status', '')
    nrdpmnmp.send.search_minor_type = request.GET.get('s_minor_type', '')
    nrdpmnmp.send.search_school = request.GET.get('s_school', '')
    nrdpmnmp.send.search_field_of_study = request.GET.get('s_field_of_study', '')
 
    nrdpmnmp.send.action = request.GET.get('action', '') 
    nrdpmnmp.send.sequence_nbr = request.GET.get('sequence_nbr', '')
    nrdpmnmp.send.start_isn = request.GET.get('start_isn', '')
    
#    nrdpmnmp.send.ip_address = request.META['REMOTE_ADDR']   
    
# **************************************************************************** #
#                Broker Call 
# **************************************************************************** #

    try:     
        nrdpmnmp.call_broker_once(service=request.META['HTTP_SERVICE'])

    except (UTBrokerError), error_info:
        exception_msg = str(error_info)
        return render_to_response('error.html', UTDirectContext(request,
            {'exception_msg': exception_msg},
            defaults=PROJECT_UTD_DEFAULTS,
            document_title = 'Broker Error',))
        
# **************************************************************************** #
#                Display
# **************************************************************************** #       
    context = {}

    # this is all used for debug
    pda_send_dict = OrderedDict()
    pda_recv_dict = OrderedDict()
    for field in nrdpmnmp.send:
        pda_send_dict[field] = getattr(nrdpmnmp.send, field)
    for field in nrdpmnmp.recv:
        pda_recv_dict[field] = getattr(nrdpmnmp.recv, field)
    context['pda_send_dict'] = pda_send_dict
    context['pda_recv_dict'] = pda_recv_dict
    context['pda_meta_dict'] = {'envo': request.META['HTTP_SERVICE'] }

    context ['recv'] = nrdpmnmp.recv
    context ['send'] = nrdpmnmp.send
    
    if nrdpmnmp.recv.auth_to_change == 'X':
        defaults = PROJECT_UTD_DEFAULTS_AUTH
    else:
        defaults = PROJECT_UTD_DEFAULTS
    
    return render_to_response("minor_inv_home.html", UTDirectContext(request, context, defaults=defaults))
