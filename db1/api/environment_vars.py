"""Environment variables used in the api package."""

import os

DB1_HTTP_URL = "https://item.db1.io"
DB1_WS_URL = "wss://item-ws.db1.io"

DB1_HTTP_URL_KEY = "DB1_HTTP_URL"
DB1_WS_URL_KEY = "DB1_WS_URL"

if os.environ.get(DB1_HTTP_URL_KEY) is not None:
    DB1_HTTP_URL = os.environ[DB1_HTTP_URL_KEY]

if os.environ.get(DB1_WS_URL_KEY) is not None:
    DB1_WS_URL = os.environ[DB1_WS_URL_KEY]

DB1_HTTP_CREATE_ENDPOINT = DB1_HTTP_URL + "/create"
DB1_HTTP_SET_ENDPOINT = DB1_HTTP_URL + "/set"
DB1_HTTP_GET_ENDPOINT = DB1_HTTP_URL + "/get"
DB1_HTTP_DELETE_ENDPOINT = DB1_HTTP_URL + "/delete"
DB1_HTTP_UPDATE_METAVARIABLES_ENDPOINT = DB1_HTTP_URL + "/update_metavaribles"
