# -*- coding: utf-8 -*-


def generate_secret():
    pass


def compute_hmac(request):
    host = JODEL_API_HOST
    port = JODEL_API_PORT
    path = ""

    # Concatenate the host, port number and request path.
    blob = "{host}%{port}%{path}".format(host=host, port=port, path=path)

    # Append some of the "Authorization" header if present.
    auth = None
    try:
        auth = request.headers["Authorization"]
    except KeyError:
        pass
    if auth:
        blob += "%{authorization}".format(authorization=auth.split(" ")[1])

    # Append the current time formatted as ISO 8601 with the offset from UTC.
    #  - Format : "YYYY-MM-DDTHH:MM:SSZ"
    #  - Example: "2016-04-03T13:12:38Z"
    blob += "{timestamp}".format(timestamp=request.headers["X-Timestamp"])
