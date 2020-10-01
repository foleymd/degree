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


class Nrdpscrl(Pda):
    # ************************************************************************************************
    # Python class Nrdpscrl generated using information on the fields in
    # pda nrdpscrl in library NRCAWS (TEST).
    # Created by Marjorie D Foley on Thu Aug 18 09:33:11 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 60
    RECV_LENGTH = 4668
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCRL'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        paging_isn = NaturalNumeric(offset=44, int_digits=10, dec_digits=0)
        paging_effective_ccyys = NaturalNumeric(offset=54, int_digits=5, dec_digits=0)
        form_submitted = NaturalAlpha(offset=59, length=1)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        security_level = NaturalAlpha(offset=304, length=20)
        recs_returned = FieldGroupArray(
            fields=["eid", "sri", "name", "doc_nbr", "type", "credential_code", "credential_desc_long", "status",
                    "pursuing", "catalog_beg", "catalog_end", "effective_ccyys", "conferred_ccyys"], dimensions=[25])
        eid = NaturalAlpha(offset=324, length=8, dims=(Dim(25, 173),))
        sri = NaturalAlpha(offset=332, length=9, dims=(Dim(25, 173),))
        name = NaturalAlpha(offset=341, length=25, dims=(Dim(25, 173),))
        doc_nbr = NaturalAlpha(offset=366, length=10, dims=(Dim(25, 173),))
        type = NaturalAlpha(offset=376, length=11, dims=(Dim(25, 173),))
        credential_code = NaturalAlpha(offset=387, length=8, dims=(Dim(25, 173),))
        credential_desc_long = NaturalAlpha(offset=395, length=50, dims=(Dim(25, 173),))
        status = NaturalAlpha(offset=445, length=31, dims=(Dim(25, 173),))
        pursuing = NaturalAlpha(offset=476, length=1, dims=(Dim(25, 173),))
        catalog_beg = NaturalAlpha(offset=477, length=5, dims=(Dim(25, 173),))
        catalog_end = NaturalAlpha(offset=482, length=5, dims=(Dim(25, 173),))
        effective_ccyys = NaturalAlpha(offset=487, length=5, dims=(Dim(25, 173),))
        conferred_ccyys = NaturalAlpha(offset=492, length=5, dims=(Dim(25, 173),))
        nbr_recs_returned = NaturalNumeric(offset=4649, int_digits=2, dec_digits=0)
        paging_isn = NaturalNumeric(offset=4651, int_digits=10, dec_digits=0)
        paging_effective_ccyys = NaturalNumeric(offset=4661, int_digits=5, dec_digits=0)
        is_reg_admin = NaturalAlpha(offset=4666, length=1)
        last_send_field = NaturalAlpha(offset=4667, length=1)