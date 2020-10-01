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


class Nrdpscrr(Pda):
    # ************************************************************************************************
    # Python class Nrdpscrr generated using information on the fields in
    # pda nrdpscrr in library NRCAWS (TEST).
    # Created by Marjorie D Foley on Mon Aug 15 20:47:10 CDT 2016.
    # ************************************************************************************************
    SEND_LENGTH = 74
    RECV_LENGTH = 5349
    DEFAULT_SERVER_NAME = 'NR-CRED'
    DEFAULT_SUBPROGRAM = 'NRNPSCRR'

    class Send:
        subprogram_to_call = NaturalAlpha(offset=0, length=8)
        webtoken = NaturalAlpha(offset=8, length=36)
        eid = NaturalAlpha(offset=44, length=8)
        paging_isn = NaturalNumeric(offset=52, int_digits=10, dec_digits=0)
        file_paging_isn = NaturalNumeric(offset=62, int_digits=10, dec_digits=0)
        paging_data_source = NaturalAlpha(offset=72, length=1)
        form_submitted = NaturalAlpha(offset=73, length=1)

    class Recv:
        server_error_data = NaturalAlpha(offset=0, length=100)
        return_code = NaturalAlpha(offset=100, length=4)
        return_msg = NaturalAlpha(offset=104, length=200)
        security_level = NaturalAlpha(offset=304, length=20)
        recs_returned = FieldGroupArray(
            fields=["eid", "sri", "name", "doc_nbr", "status", "type", "credential_code", "credential_desc_long",
                    "pursuing", "catalog_beg", "catalog_end", "effective_ccyys", "conferred_ccyys"], dimensions=[25])
        eid = NaturalAlpha(offset=324, length=8, dims=(Dim(25, 200),))
        sri = NaturalAlpha(offset=332, length=9, dims=(Dim(25, 200),))
        name = NaturalAlpha(offset=341, length=50, dims=(Dim(25, 200),))
        doc_nbr = NaturalAlpha(offset=391, length=10, dims=(Dim(25, 200),))
        status = NaturalAlpha(offset=401, length=31, dims=(Dim(25, 200),))
        type = NaturalAlpha(offset=432, length=11, dims=(Dim(25, 200),))
        credential_code = NaturalAlpha(offset=443, length=10, dims=(Dim(25, 200),))
        credential_desc_long = NaturalAlpha(offset=453, length=50, dims=(Dim(25, 200),))
        pursuing = NaturalAlpha(offset=503, length=1, dims=(Dim(25, 200),))
        catalog_beg = NaturalAlpha(offset=504, length=5, dims=(Dim(25, 200),))
        catalog_end = NaturalAlpha(offset=509, length=5, dims=(Dim(25, 200),))
        effective_ccyys = NaturalAlpha(offset=514, length=5, dims=(Dim(25, 200),))
        conferred_ccyys = NaturalAlpha(offset=519, length=5, dims=(Dim(25, 200),))
        nbr_recs_returned = NaturalAlpha(offset=5324, length=2)
        paging_isn = NaturalNumeric(offset=5326, int_digits=10, dec_digits=0)
        file_paging_isn = NaturalNumeric(offset=5336, int_digits=10, dec_digits=0)
        paging_data_source = NaturalAlpha(offset=5346, length=1)
        is_reg_admin = NaturalAlpha(offset=5347, length=1)
        last_send_field = NaturalAlpha(offset=5348, length=1)