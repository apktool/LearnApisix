import requests

url_prefix = "http://localhost:9180/apisix/admin"

headers = {
    "X-API-KEY": "edd1c9f034335f136f87ad84b625c8f1"
}


def list_route():
    url = f"{url_prefix}/routes"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()


def add_route(ids: str, config: dict):
    url = f"{url_prefix}/routes/{ids}"
    response = requests.put(url, json=config, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()


def delete_route(ids: str):
    url = f"{url_prefix}/routes/{ids}"
    response = requests.delete(url, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()


def list_upstream():
    url = f"{url_prefix}/upstreams"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()


def add_upstream(ids: str, config: dict):
    url = f"{url_prefix}/upstreams/{ids}"
    response = requests.put(url, json=config, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()


def delete_upstream(ids: str):
    url = f"{url_prefix}/upstreams/{ids}"
    response = requests.delete(url, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: {response.text}")
        return {}
    else:
        return response.json()
