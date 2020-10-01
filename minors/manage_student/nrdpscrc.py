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


class Nrdpscrc(Pda):
    # ************************************************************************************************
    # Python class Nrdpscrc generated using information on the fields in
    # pda nrdpscrc in library NRCAWS (TEST).
    # Created by Marjorie D Foley on Mon Aug 29 15:42:03 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 82
    RECV_LENGTH = 3269
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCRC'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        status = NaturalAlpha(offset=44, length=1)
        credential_code = NaturalAlpha(offset=45, length=8)
        type = NaturalAlpha(offset=45, length=2)
        school = NaturalAlpha(offset=47, length=1)
        fos = NaturalAlpha(offset=48, length=3)
        seq = NaturalAlpha(offset=51, length=2)
        paging_isn = NaturalNumeric(offset=53, int_digits=10, dec_digits=0)
        paging_effective_ccyys = NaturalNumeric(offset=63, int_digits=5, dec_digits=0)
        paging_time = NaturalAlpha(offset=68, length=13)
        form_submitted = NaturalAlpha(offset=81, length=1)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        recs_returned = FieldGroupArray(
            fields=["eid", "sri", "name", "doc_nbr", "type", "status", "pursuing", "catalog_beg", "catalog_end",
                    "effective_ccyys", "conferred_ccyys"], dimensions=[25])
        eid = NaturalAlpha(offset=304, length=8, dims=(Dim(25, 115),))
        sri = NaturalAlpha(offset=312, length=9, dims=(Dim(25, 115),))
        name = NaturalAlpha(offset=321, length=25, dims=(Dim(25, 115),))
        doc_nbr = NaturalAlpha(offset=346, length=10, dims=(Dim(25, 115),))
        type = NaturalAlpha(offset=356, length=11, dims=(Dim(25, 115),))
        status = NaturalAlpha(offset=367, length=31, dims=(Dim(25, 115),))
        pursuing = NaturalAlpha(offset=398, length=1, dims=(Dim(25, 115),))
        catalog_beg = NaturalAlpha(offset=399, length=5, dims=(Dim(25, 115),))
        catalog_end = NaturalAlpha(offset=404, length=5, dims=(Dim(25, 115),))
        effective_ccyys = NaturalAlpha(offset=409, length=5, dims=(Dim(25, 115),))
        conferred_ccyys = NaturalAlpha(offset=414, length=5, dims=(Dim(25, 115),))
        credential_code = NaturalAlpha(offset=3179, length=8)
        credential_desc_long = NaturalAlpha(offset=3187, length=50)
        nbr_recs_returned = NaturalNumeric(offset=3237, int_digits=2, dec_digits=0)
        paging_isn = NaturalNumeric(offset=3239, int_digits=10, dec_digits=0)
        paging_effective_ccyys = NaturalNumeric(offset=3249, int_digits=5, dec_digits=0)
        paging_time = NaturalAlpha(offset=3254, length=13)
        is_reg_admin = NaturalAlpha(offset=3267, length=1)
        last_send_field = NaturalAlpha(offset=3268, length=1)
