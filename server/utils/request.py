import json


def get_request_data(request):
    try:
        return json.loads(request.body.decode("utf-8"))

    except (
        json.JSONDecodeError,
        UnicodeDecodeError,
    ):
        return {}
