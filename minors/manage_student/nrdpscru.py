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


class Nrdpscru(Pda):
    # ************************************************************************************************
    # Python class Nrdpscru generated using information on the fields in
    # pda nrdpscru in library NRCAWS (TEST).
    # Created by Marjorie D Foley on Tue Aug 30 13:35:44 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 414
    RECV_LENGTH = 2810
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCRU'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        security_level = NaturalAlpha(offset=44, length=20)
        update = NaturalAlpha(offset=64, length=1)
        sri = NaturalNumeric(offset=65, int_digits=9, dec_digits=0)
        doc_nbr = NaturalNumeric(offset=74, int_digits=10, dec_digits=0)
        status = NaturalAlpha(offset=84, length=1)
        catalog_beg = NaturalAlpha(offset=85, length=5)
        catalog_beg_ccyy = NaturalAlpha(offset=85, length=4)
        catalog_beg_s = NaturalAlpha(offset=89, length=1)
        catalog_end = NaturalAlpha(offset=90, length=5)
        catalog_end_ccyy = NaturalNumeric(offset=90, int_digits=4, dec_digits=0)
        catalog_end_s = NaturalNumeric(offset=94, int_digits=1, dec_digits=0)
        created_date = NaturalAlpha(offset=95, length=10)
        created_id = NaturalAlpha(offset=105, length=8)
        effective_ccyys = NaturalAlpha(offset=113, length=5)
        effective_ccyy = NaturalNumeric(offset=113, int_digits=4, dec_digits=0)
        effective_s = NaturalNumeric(offset=117, int_digits=1, dec_digits=0)
        coursework_satisfied_date = NaturalAlpha(offset=118, length=10)
        coursework_satisfied_id = NaturalAlpha(offset=128, length=8)
        coursework_satisfied_ccyys = NaturalAlpha(offset=136, length=5)
        coursework_satisfied_ccyy = NaturalNumeric(offset=136, int_digits=4, dec_digits=0)
        coursework_satisfied_s = NaturalNumeric(offset=140, int_digits=1, dec_digits=0)
        conferred_date = NaturalAlpha(offset=141, length=10)
        conferred_id = NaturalAlpha(offset=151, length=8)
        conferred_ccyys = NaturalAlpha(offset=159, length=5)
        conferred_ccyy = NaturalNumeric(offset=159, int_digits=4, dec_digits=0)
        conferred_s = NaturalNumeric(offset=163, int_digits=1, dec_digits=0)
        comments = NaturalAlpha(offset=164, length=250)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        student = FieldGroup(
            fields=["sri", "eid", "name", "doc_nbr", "status", "credential_code", "credential_desc_long", "catalog_beg",
                    "catalog_end", "created_date", "created_id", "created_name", "effective_ccyys",
                    "coursework_satisfied_date", "coursework_satisfied_id", "coursework_satisfied_name",
                    "coursework_satisfied_ccyys", "conferred_date", "conferred_id", "conferred_name", "conferred_ccyys",
                    "comment_array", "degree_array", "last_undergrad_ccyys", "last_pharmacy_ccyys", "auth_to_edit",
                    "auth_to_view", "is_reg_admin", "last_send_field"])
        sri = NaturalNumeric(offset=304, int_digits=9, dec_digits=0)
        eid = NaturalAlpha(offset=313, length=8)
        name = NaturalAlpha(offset=321, length=50)
        doc_nbr = NaturalNumeric(offset=371, int_digits=10, dec_digits=0)
        status = NaturalAlpha(offset=381, length=1)
        credential_code = NaturalAlpha(offset=382, length=8)
        type = NaturalAlpha(offset=382, length=2)
        school = NaturalAlpha(offset=384, length=1)
        fos = NaturalAlpha(offset=385, length=3)
        seq = NaturalAlpha(offset=388, length=2)
        credential_desc_long = NaturalAlpha(offset=390, length=50)
        catalog_beg = NaturalAlpha(offset=440, length=5)
        catalog_beg_ccyy = NaturalAlpha(offset=440, length=4)
        catalog_beg_s = NaturalAlpha(offset=444, length=1)
        catalog_end = NaturalAlpha(offset=445, length=5)
        catalog_end_ccyy = NaturalNumeric(offset=445, int_digits=4, dec_digits=0)
        catalog_end_s = NaturalNumeric(offset=449, int_digits=1, dec_digits=0)
        created_date = NaturalAlpha(offset=450, length=10)
        created_id = NaturalAlpha(offset=460, length=8)
        created_name = NaturalAlpha(offset=468, length=50)
        effective_ccyys = NaturalAlpha(offset=518, length=5)
        effective_ccyy = NaturalNumeric(offset=518, int_digits=4, dec_digits=0)
        effective_s = NaturalNumeric(offset=522, int_digits=1, dec_digits=0)
        coursework_satisfied_date = NaturalAlpha(offset=523, length=10)
        coursework_satisfied_id = NaturalAlpha(offset=533, length=8)
        coursework_satisfied_name = NaturalAlpha(offset=541, length=50)
        coursework_satisfied_ccyys = NaturalAlpha(offset=591, length=5)
        coursework_satisfied_ccyy = NaturalNumeric(offset=591, int_digits=4, dec_digits=0)
        coursework_satisfied_s = NaturalNumeric(offset=595, int_digits=1, dec_digits=0)
        conferred_date = NaturalAlpha(offset=596, length=10)
        conferred_id = NaturalAlpha(offset=606, length=8)
        conferred_name = NaturalAlpha(offset=614, length=50)
        conferred_ccyys = NaturalAlpha(offset=664, length=5)
        conferred_ccyy = NaturalNumeric(offset=664, int_digits=4, dec_digits=0)
        conferred_s = NaturalNumeric(offset=668, int_digits=1, dec_digits=0)
        comment_array = FieldGroupArray(
            fields=["comments", "commenter_id", "commenter_name", "comment_date", "comment_status"], dimensions=[5])
        comments = NaturalAlpha(offset=669, length=250, dims=(Dim(5, 319),))
        commenter_id = NaturalAlpha(offset=919, length=8, dims=(Dim(5, 319),))
        commenter_name = NaturalAlpha(offset=927, length=50, dims=(Dim(5, 319),))
        comment_date = NaturalAlpha(offset=977, length=10, dims=(Dim(5, 319),))
        comment_status = NaturalAlpha(offset=987, length=1, dims=(Dim(5, 319),))
        degree_array = FieldGroupArray(fields=["degree", "degree_ccyys", "degree_major"], dimensions=[7])
        degree = NaturalAlpha(offset=2264, length=16, dims=(Dim(7, 76),))
        degree_ccyys = NaturalAlpha(offset=2280, length=5, dims=(Dim(7, 76),))
        degree_ccyy = NaturalNumeric(offset=2280, int_digits=4, dec_digits=0, dims=(Dim(7, 76),))
        degree_s = NaturalNumeric(offset=2284, int_digits=1, dec_digits=0, dims=(Dim(7, 76),))
        degree_major = NaturalAlpha(offset=2285, length=55, dims=(Dim(7, 76),))
        last_undergrad_ccyys = NaturalAlpha(offset=2796, length=5)
        last_pharmacy_ccyys = NaturalAlpha(offset=2801, length=5)
        auth_to_edit = NaturalAlpha(offset=2806, length=1)
        auth_to_view = NaturalAlpha(offset=2807, length=1)
        is_reg_admin = NaturalAlpha(offset=2808, length=1)
        last_send_field = NaturalAlpha(offset=2809, length=1)

