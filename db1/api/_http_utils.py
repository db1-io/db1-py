"""HTTP helper function for api package."""

import requests

from db1.api import exceptions


def make_http_request(url: str, data: bytes):
    """Make an http request."""
    try:
        http_response = requests.post(
            url=url, data=data, headers={"Content-Type": "application/octet-stream"}
        )
        http_response.raise_for_status()
    except Exception as error:
        raise exceptions.HttpError(error)

    return http_response
