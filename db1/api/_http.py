"""HTTP helper function for api package."""

import requests


def make_http_request(url: str, data: bytes):
    """Make an http request."""
    http_response = requests.post(
        url=url, data=data, headers={"Content-Type": "application/octet-stream"}
    )
    return http_response
