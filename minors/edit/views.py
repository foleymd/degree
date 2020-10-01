from django.shortcuts import render_to_response
from django.utils.datastructures import OrderedDict

from utbroker.errors import UTBrokerError
from utdirect.templates import UTDirectContext

from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS_AUTH
from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS
from degree.minors.settings import STATIC_URL
from degree.minors.edit.nrdpmnmn import Nrdpmnmn

          
# *************************************************************************** #
#                  Main Function                                                                                    
# *************************************************************************** #

def edit(request, stat_ty_schl_fos_seq):                             
                                                                                         
    nrdpmnmn= Nrdpmnmn()                                                                                

    nrdpmnmn.send.webtoken = request.META['HTTP_TOKEN']      
    nrdpmnmn.send.stat_ty_schl_fos_seq = stat_ty_schl_fos_seq
    nrdpmnmn.send.lo_ccyys = request.POST.get('lo_ccyys', '')
    nrdpmnmn.send.hi_ccyys = request.POST.get('hi_ccyys', '')
    nrdpmnmn.send.max_students = request.POST.get('max_students', '')
    nrdpmnmn.send.total_hours = request.POST.get('total_hours', '')
    nrdpmnmn.send.desc_short = request.POST.get('desc_short', '').encode('ascii', 'ignore')
    nrdpmnmn.send.desc_long = request.POST.get('desc_long', '').encode('ascii', 'ignore')
    nrdpmnmn.send.auto_approve = request.POST.get('auto_approve', '')
    nrdpmnmn.send.cip_code = request.POST.get('cip_code', '').encode('ascii', 'ignore')
    nrdpmnmn.send.cred_level = request.POST.get('cred_level', '')
    nrdpmnmn.send.url = request.POST.get('url', '').encode('ascii', 'ignore')
    nrdpmnmn.send.on_off_sw = request.POST.get('on_off_sw', '')
    nrdpmnmn.send.cohort_description = request.POST.get('cohort_description', '').encode('ascii', 'ignore')
    nrdpmnmn.send.related_major_code[0] = request.POST.get('related_major_code_1', '')
    nrdpmnmn.send.related_major_code[1] = request.POST.get('related_major_code_2', '')
    nrdpmnmn.send.related_major_code[2] = request.POST.get('related_major_code_3', '')
    nrdpmnmn.send.related_major_code[3] = request.POST.get('related_major_code_4', '')
    nrdpmnmn.send.related_major_code[4] = request.POST.get('related_major_code_5', '')
    nrdpmnmn.send.related_major_code[5] = request.POST.get('related_major_code_6', '')
    nrdpmnmn.send.related_major_code[6] = request.POST.get('related_major_code_7', '')
    nrdpmnmn.send.related_major_code[7] = request.POST.get('related_major_code_8', '')
    nrdpmnmn.send.related_major_code[8] = request.POST.get('related_major_code_9', '')
    nrdpmnmn.send.related_major_code[9] = request.POST.get('related_major_code_10', '')
    nrdpmnmn.send.action = request.POST.get('deactivate_sw', '')
    
    if nrdpmnmn.send.stat_ty_schl_fos_seq == '':
        nrdpmnmn.send.minor_type = request.POST.get('minor_type', '')
        nrdpmnmn.send.school = request.POST.get('school', '')
        nrdpmnmn.send.field_of_study = request.POST.get('field_of_study', '')
        nrdpmnmn.send.sequence_nbr = request.POST.get('sequence_nbr', '')
    
    if request.method == 'POST':
        if 'update' in request.POST:
            nrdpmnmn.send.action = "U"
        elif 'create' in request.POST:
            nrdpmnmn.send.action = "S"         
    
#    nrdpmnmp.send.ip_address = request.META['REMOTE_ADDR']   
    
# **************************************************************************** #
#                Broker Call 
# **************************************************************************** #

    try:     
        nrdpmnmn.call_broker_once(service=request.META['HTTP_SERVICE'])

    except (UTBrokerError), error_info:
        exception_msg = str(error_info)
        return render_to_response('error.html', UTDirectContext(request,
            {'exception_msg': exception_msg},
            defaults=defaults,
            document_title = 'Broker Error',))
        
# **************************************************************************** #
#                Display
# **************************************************************************** #       
    context = {}

    # this is all used for debug
    pda_send_dict = OrderedDict()
    pda_recv_dict = OrderedDict()
    for field in nrdpmnmn.send:
        pda_send_dict[field] = getattr(nrdpmnmn.send, field)
    for field in nrdpmnmn.recv:
        pda_recv_dict[field] = getattr(nrdpmnmn.recv, field)
    context['pda_send_dict'] = pda_send_dict
    context['pda_recv_dict'] = pda_recv_dict
    context['pda_meta_dict'] = {'envo': request.META['HTTP_SERVICE'] }

    context ['recv'] = nrdpmnmn.recv
    context ['send'] = nrdpmnmn.send
    
    if nrdpmnmn.recv.auth_to_change == 'X':
        defaults = PROJECT_UTD_DEFAULTS_AUTH
    else:
        defaults = PROJECT_UTD_DEFAULTS
    
    return render_to_response("edit.html", UTDirectContext(request, context, defaults=defaults))
