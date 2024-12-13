from . import config
from ._api_call import Request


class USSD:
    @staticmethod
    def get_banks():
        url = f"{config.API_URL}/payment/ussd/supported-banks"
        return Request.call(Request.Method.GET, url)

    @staticmethod
    def request_code(transaction_ref: str, bank_name: str):
        url = f"{config.API_URL}/payment/ussd/request-ussd-code/{transaction_ref}"
        data = {"bank_name": bank_name}
        return Request.call(Request.Method.POST, url, data=data)
