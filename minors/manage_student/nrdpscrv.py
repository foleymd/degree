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


class Nrdpscrv(Pda):
    # ************************************************************************************************
    # Python class Nrdpscrv generated using information on the fields in
    # pda NRDPSCRV in library NRCAWS (TEST).
    # Created by Marjorie D Foley on Fri Sep 30 11:33:16 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 56
    RECV_LENGTH = 456
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCRV'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        form_submitted = NaturalAlpha(offset=44, length=1)
        counts_submitted = NaturalAlpha(offset=45, length=1)
        code_or_eid_submitted = NaturalAlpha(offset=46, length=1)
        code_or_eid_input = NaturalAlpha(offset=47, length=9)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        job_info = FieldGroup(fields=["job_names", "job_numbers"])
        job_names = NaturalAlpha(offset=304, length=8, dims=(Dim(10, 8),))
        job_numbers = NaturalAlpha(offset=384, length=7, dims=(Dim(10, 7),))
        is_reg_admin = NaturalAlpha(offset=454, length=1)
        last_send_field = NaturalAlpha(offset=455, length=1)