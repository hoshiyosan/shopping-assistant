from fastapi import HTTPException


class ApiError(HTTPException):
    def __init__(self, *, error, status=500, **info):
        super().__init__(detail={"message": error, **info}, status_code=status)


class AuthenticationError(ApiError):
    def __init__(self, *, error, **info):
        super().__init__(error=error, status=401, **info)


class ObjectNotFound(ApiError):
    def __init__(self, *, error, **info):
        super().__init__(error=error, status=404, **info)


class ObjectAlreadyExists(ApiError):
    def __init__(self, *, error, **info):
        super().__init__(error=error, status=409, **info)
