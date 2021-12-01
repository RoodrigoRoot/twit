from rest_framework.exceptions import APIException


class FollowItSelfException(APIException):
    status_code = 400


class DoubleFollowException(APIException):
    status_code = 400


class PasswordAreDifferentException(APIException):
    status_code = 400


class UsernameExistsException(APIException):
    status_code = 400


class EmailExistsException(APIException):
    status_code = 400
