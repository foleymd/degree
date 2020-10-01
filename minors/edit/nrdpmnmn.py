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


class Nrdpmnmn(Pda):
# ************************************************************************************************
# Python class Nrdpmnmn generated using information on the fields in
# pda NRDPMNMN in library NRDAUD (TEST).
# Created by Brian E Ruh on Fri Sep 02 10:41:26 CDT 2016.
# ************************************************************************************************
    SEND_LENGTH = 650
    RECV_LENGTH = 1188
    DEFAULT_SERVER_NAME = 'NR-MINORS'
    DEFAULT_SUBPROGRAM = 'NRNPMNMN'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        action = NaturalAlpha(offset=44, length=1)
        stat_ty_schl_fos_seq = NaturalAlpha(offset=45, length=9)
        status = NaturalAlpha(offset=45, length=1)
        minor_type = NaturalAlpha(offset=46, length=2)
        school = NaturalAlpha(offset=48, length=1)
        field_of_study = NaturalAlpha(offset=49, length=3)
        sequence_nbr = NaturalAlpha(offset=52, length=2)
        related_major_code = NaturalAlpha(offset=54, length=6, dims=(Dim(10, 6),))
        total_hours = NaturalAlpha(offset=114, length=3)
        lo_ccyys = NaturalAlpha(offset=117, length=5)
        hi_ccyys = NaturalAlpha(offset=122, length=5)
        max_students = NaturalAlpha(offset=127, length=7)
        desc_short = NaturalAlpha(offset=134, length=50)
        desc_long = NaturalAlpha(offset=184, length=100)
        auto_approve = NaturalAlpha(offset=284, length=1)
        cip_code = NaturalAlpha(offset=285, length=13)
        cred_level = NaturalAlpha(offset=298, length=1)
        url = NaturalAlpha(offset=299, length=250)
        on_off_sw = NaturalAlpha(offset=549, length=1)
        cohort_description = NaturalAlpha(offset=550, length=100)
            
    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        error_code = NaturalAlpha(offset=100, length=4)
        return_code = NaturalAlpha(offset=104, length=4)
        return_msg = NaturalAlpha(offset=108, length=100)
        debug_string = NaturalAlpha(offset=208, length=200)
        debug_sw = NaturalAlpha(offset=408, length=1)
        auth_to_view = NaturalAlpha(offset=409, length=1)
        auth_to_change = NaturalAlpha(offset=410, length=1)
        auth_to_turn_on_off = NaturalAlpha(offset=411, length=1)
        user_role = NaturalAlpha(offset=412, length=3)
        status = NaturalAlpha(offset=415, length=1)
        cred_code = NaturalAlpha(offset=416, length=8)
        minor_type = NaturalAlpha(offset=424, length=2)
        minor_type_desc = NaturalAlpha(offset=426, length=11)
        school = NaturalAlpha(offset=437, length=1)
        school_desc = NaturalAlpha(offset=438, length=25)
        field_of_study = NaturalAlpha(offset=463, length=3)
        sequence_nbr = NaturalAlpha(offset=466, length=2)
        major_short_desc = NaturalAlpha(offset=468, length=16, dims=(Dim(10, 16),))
        total_hours = NaturalAlpha(offset=628, length=3)
        lo_ccyys = NaturalAlpha(offset=631, length=5)
        hi_ccyys = NaturalAlpha(offset=636, length=5)
        max_students = NaturalAlpha(offset=641, length=7)
        desc_short = NaturalAlpha(offset=648, length=50)
        desc_long = NaturalAlpha(offset=698, length=100)
        auto_approve = NaturalAlpha(offset=798, length=1)
        auto_approve_desc = NaturalAlpha(offset=799, length=3)
        cip_code = NaturalAlpha(offset=802, length=13)
        cred_level = NaturalAlpha(offset=815, length=1)
        cred_level_desc = NaturalAlpha(offset=816, length=13)
        url = NaturalAlpha(offset=829, length=250)
        on_off_sw = NaturalAlpha(offset=1079, length=1)
        on_off_sw_desc = NaturalAlpha(offset=1080, length=3)
        cohort_description = NaturalAlpha(offset=1083, length=100)
        no_update_made = NaturalAlpha(offset=1183, length=1)
        success_update = NaturalAlpha(offset=1184, length=1)
        success_store = NaturalAlpha(offset=1185, length=1)
        success_deactivation = NaturalAlpha(offset=1186, length=1)
        last_send_field = NaturalAlpha(offset=1187, length=1)
