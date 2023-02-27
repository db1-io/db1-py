"""Exceptions used in the api package."""


# General


class DB1ApiError(Exception):
    """Base class for all db1 api errors."""


class HttpError(DB1ApiError):
    """Used to indicate an http error."""


class InternalServerError(DB1ApiError):
    """Used to indicate internal server error."""


class BadRequestError(DB1ApiError):
    """Used to indicate bad request error."""


# Item


class AlreadyExistsError(DB1ApiError):
    """Used to indicate that a resource already exists."""


class NotFoundError(DB1ApiError):
    """Used to indicate that a resource does not exist."""


class ItemValueTooBigError(DB1ApiError):
    """Used to indicate that an item value is larger than `max_size_bytes`."""


class InvalidKeyError(DB1ApiError):
    """Used to indicate that a resource ID is invalid."""
