from django.utils.encoding import force_text
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['error_type'] = response.data.pop('detail')

    return response


class Z3Exception(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Z3 Error'

    def __init__(self, detail: object, field: object, status_code: object) -> object:
        if status_code is not None: self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}
