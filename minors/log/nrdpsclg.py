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


class Nrdpsclg(Pda):
    # ************************************************************************************************
    # Python class Nrdpsclg generated using information on the fields in
    # pda NRDPSCLG in library NRCAWS (TEST).
    # Created by Sara Denise Gore on Wed Sep 14 10:59:46 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 77
    RECV_LENGTH = 12225
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCLG'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        search_eid = NaturalAlpha(offset=44, length=8)
        paging_isn = NaturalNumeric(offset=52, int_digits=10, dec_digits=0)
        paging_create_date_cymd = NaturalNumeric(offset=62, int_digits=8, dec_digits=0)
        paging_create_time = NaturalNumeric(offset=70, int_digits=7, dec_digits=0)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        search_eid = NaturalAlpha(offset=304, length=8)
        name = NaturalAlpha(offset=312, length=25)
        recs_returned = FieldGroupArray(
            fields=["log_id", "log_code", "log_desc", "doc_nbr", "credential_code",
                    "old_value", "new_value", "create_id", "create_date_cymd",
                    "create_time"], dimensions=[20])
        log_id = NaturalAlpha(offset=337, length=15, dims=(Dim(20, 593),))
        log_code = NaturalAlpha(offset=352, length=5, dims=(Dim(20, 593),))
        log_desc = NaturalAlpha(offset=357, length=30, dims=(Dim(20, 593),))
        doc_nbr = NaturalAlpha(offset=387, length=10, dims=(Dim(20, 593),))
        credential_code = NaturalAlpha(offset=397, length=10, dims=(Dim(20, 593),))
        old_value = NaturalAlpha(offset=407, length=250, dims=(Dim(20, 593),))
        new_value = NaturalAlpha(offset=657, length=250, dims=(Dim(20, 593),))
        create_id = NaturalAlpha(offset=907, length=8, dims=(Dim(20, 593),))
        create_date_cymd = NaturalNumeric(offset=915, int_digits=8, dec_digits=0,
                                          dims=(Dim(20, 593),))
        create_time = NaturalNumeric(offset=923, int_digits=7, dec_digits=0,
                                     dims=(Dim(20, 593),))
        nbr_recs_returned = NaturalAlpha(offset=12197, length=2)
        paging_isn = NaturalNumeric(offset=12199, int_digits=10, dec_digits=0)
        paging_create_date_cymd = NaturalNumeric(offset=12209, int_digits=8, dec_digits=0)
        paging_create_time = NaturalNumeric(offset=12217, int_digits=7, dec_digits=0)
        last_send_field = NaturalAlpha(offset=12224, length=1)


