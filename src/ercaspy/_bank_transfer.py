from . import config
from ._api_call import Request


class BankTransfer:
    @staticmethod
    def request_account(transaction_ref: str):
        url = f"{config.API_URL}/payment/bank-transfer/request-bank-account/{transaction_ref}"
        return Request.call(Request.Method.GET, url)
