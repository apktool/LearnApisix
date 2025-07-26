from apid.apisix import list_route, add_route, list_upstream, add_upstream
import json


def test_list_upstream():
    response = list_upstream()
    print(json.dumps(response, indent=4))


def test_add_upstream():
    body = {
        "id": "202507261000",
        "name": "smart_upstream",
        "discovery_type": "smart_consul",
        "type": "roundrobin",
        "service_name": "http_dispatcher",
        "hash_on": "vars",
        "scheme": "http"
    }
    res = add_upstream(ids=body["id"], config=body)
    print(json.dumps(res, indent=4))

    body = {
        "id": "202507271000",
        "name": "smart_upstream",
        "discovery_type": "smart_consul",
        "type": "roundrobin",
        "service_name": "grpc_dispatcher",
        "hash_on": "vars",
        "scheme": "grpc"
    }
    res = add_upstream(ids=body["id"], config=body)
    print(json.dumps(res, indent=4))


def test_list_route():
    response = list_route()
    print(json.dumps(response, indent=4))


def test_add_route():
    body = {
        "id": "202507261000",
        "name": "smart_route",
        "upstream_id": "202507261000",
        "uris": ["/api/*"],
        "methods": ["GET", "POST"],
        "status": 1
    }
    res = add_route(ids=body["id"], config=body)
    print(json.dumps(res, indent=4))

    body = {
        "id": "202507271000",
        "name": "smart_route",
        "upstream_id": "202507271000",
        "uris": ["/canary.*"],
        "methods": ["GET", "POST"],
        "status": 1
    }
    res = add_route(ids=body["id"], config=body)
    print(json.dumps(res, indent=4))


