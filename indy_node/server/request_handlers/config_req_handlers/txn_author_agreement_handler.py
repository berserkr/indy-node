from indy_common.authorize.auth_actions import AuthActionAdd
from indy_common.authorize.auth_request_validator import WriteRequestValidator
from plenum.common.request import Request
from plenum.server.database_manager import DatabaseManager
from plenum.server.request_handlers.txn_author_agreement_handler import TxnAuthorAgreementHandler \
    as PTxnAuthorAgreementHandler


class TxnAuthorAgreementHandler(PTxnAuthorAgreementHandler):

    def __init__(self, database_manager: DatabaseManager, bls_crypto_verifier,
                 write_request_validator: WriteRequestValidator):
        super().__init__(database_manager, bls_crypto_verifier)
        self.write_request_validator = write_request_validator

    def dynamic_validation(self, request: Request):
        super().dynamic_validation(request)
        self.write_request_validator.validate(request,
                                              [AuthActionAdd(txn_type=self.txn_type,
                                                             field='*',
                                                             value='*')])

    def authorize(self, request):
        pass
