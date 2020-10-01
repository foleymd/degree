from utbroker.pda import Pda
from utbroker.fields import Dim, NaturalAlpha, NaturalNumeric, NaturalLogical
try:
    from utbroker.fields import FieldGroup, FieldGroupArray
except ImportError:
    # Backwards compatibility for utbroker library versions <1.0 that don't
    # define group fields.
    class Fake:
        def __init__(self, *args, **kwargs): pass
    FieldGroup = FieldGroupArray = Fake


class Nrdpmnmp(Pda):
# ************************************************************************************************
# Python class Nrdpmnmp generated using information on the fields in
# pda NRDPMNMP in library NRDAUD (TEST).
# Created by Brian E Ruh on Thu Sep 08 10:32:32 CDT 2016.
# ************************************************************************************************
    SEND_LENGTH = 71
    RECV_LENGTH = 9018
    DEFAULT_SERVER_NAME = 'NR-MINORS'
    DEFAULT_SUBPROGRAM = 'NRNPMNMP'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        action = NaturalAlpha(offset=44, length=1)
        status = NaturalAlpha(offset=45, length=1)
        minor_type = NaturalAlpha(offset=46, length=2)
        school = NaturalAlpha(offset=48, length=1)
        field_of_study = NaturalAlpha(offset=49, length=3)
        sequence_nbr = NaturalAlpha(offset=52, length=2)
        start_isn = NaturalAlpha(offset=54, length=10)
        search_status = NaturalAlpha(offset=64, length=1)
        search_minor_type = NaturalAlpha(offset=65, length=2)
        search_school = NaturalAlpha(offset=67, length=1)
        search_field_of_study = NaturalAlpha(offset=68, length=3)
            
    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        error_code = NaturalAlpha(offset=100, length=4)
        auth_to_view = NaturalAlpha(offset=104, length=1)
        auth_to_change = NaturalAlpha(offset=105, length=1)
        return_code = NaturalAlpha(offset=106, length=4)
        return_msg = NaturalAlpha(offset=110, length=100)
        debug_string = NaturalAlpha(offset=210, length=200)
        debug_sw = NaturalAlpha(offset=410, length=1)
        search_status = NaturalAlpha(offset=411, length=1)
        search_minor_type = NaturalAlpha(offset=412, length=2)
        search_school = NaturalAlpha(offset=414, length=1)
        search_field_of_study = NaturalAlpha(offset=415, length=3)
        user_role = NaturalAlpha(offset=418, length=3)
        nbr_recs_returned = NaturalNumeric(offset=421, int_digits=2, dec_digits=0)
        minor_array = FieldGroupArray(fields=["status", "status_desc", "cred_code", "minor_type", "minor_type_desc", "school", "school_desc", "field_of_study", "sequence_nbr", "desc_short", "desc_long", "cohort_description", "auto_approve", "auto_approve_desc", "lo_ccyys", "lo_ccyys_desc", "on_off_sw", "on_off_sw_desc"], dimensions=[25])
        status = NaturalAlpha(offset=423, length=1, dims=(Dim(25, 343),))
        status_desc = NaturalAlpha(offset=424, length=11, dims=(Dim(25, 343),))
        cred_code = NaturalAlpha(offset=435, length=8, dims=(Dim(25, 343),))
        minor_type = NaturalAlpha(offset=443, length=2, dims=(Dim(25, 343),))
        minor_type_desc = NaturalAlpha(offset=445, length=11, dims=(Dim(25, 343),))
        school = NaturalAlpha(offset=456, length=1, dims=(Dim(25, 343),))
        school_desc = NaturalAlpha(offset=457, length=25, dims=(Dim(25, 343),))
        field_of_study = NaturalAlpha(offset=482, length=3, dims=(Dim(25, 343),))
        sequence_nbr = NaturalAlpha(offset=485, length=2, dims=(Dim(25, 343),))
        desc_short = NaturalAlpha(offset=487, length=50, dims=(Dim(25, 343),))
        desc_long = NaturalAlpha(offset=537, length=100, dims=(Dim(25, 343),))
        cohort_description = NaturalAlpha(offset=637, length=100, dims=(Dim(25, 343),))
        auto_approve = NaturalAlpha(offset=737, length=1, dims=(Dim(25, 343),))
        auto_approve_desc = NaturalAlpha(offset=738, length=8, dims=(Dim(25, 343),))
        lo_ccyys = NaturalAlpha(offset=746, length=5, dims=(Dim(25, 343),))
        lo_ccyys_desc = NaturalAlpha(offset=751, length=11, dims=(Dim(25, 343),))
        on_off_sw = NaturalAlpha(offset=762, length=1, dims=(Dim(25, 343),))
        on_off_sw_desc = NaturalAlpha(offset=763, length=3, dims=(Dim(25, 343),))
        next_isn = NaturalAlpha(offset=8998, length=10)
        next_status = NaturalAlpha(offset=9008, length=1)
        next_minor_type = NaturalAlpha(offset=9009, length=2)
        next_school = NaturalAlpha(offset=9011, length=1)
        next_field_of_study = NaturalAlpha(offset=9012, length=3)
        next_sequence_nbr = NaturalAlpha(offset=9015, length=2)
        last_send_field = NaturalAlpha(offset=9017, length=1)
