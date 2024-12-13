class ErcasError(Exception):
    """Base class for exceptions in this module."""

    pass


class ErcasBadRequestError(ErcasError):
    """Exception raised for errors in the request.

    Attributes:
        message -- explanation of the error
    """

    pass


class ErcasUnprocessableError(ErcasError):
    """Exception raised for errors that are not processable.

    Attributes:
        message -- explanation of the error
    """

    pass
