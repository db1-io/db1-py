"""Environment variables used in the api package."""

import os as _os

DB1_PANEL_URL = "https://db1.io"
DB1_HTTP_URL = "https://item.db1.io"
DB1_HTTP_URL_KEY = "DB1_HTTP_URL"

if _os.environ.get(DB1_HTTP_URL_KEY) is not None:
    DB1_HTTP_URL = _os.environ[DB1_HTTP_URL_KEY]

DB1_HTTP_SET_ENDPOINT = DB1_HTTP_URL + "/set"
DB1_HTTP_GET_ENDPOINT = DB1_HTTP_URL + "/get"
DB1_HTTP_DELETE_ENDPOINT = DB1_HTTP_URL + "/delete"
