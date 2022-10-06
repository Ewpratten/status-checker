
import requests


def is_host_http_ok(host: str) -> bool:
    """Check if the host is up and responding to HTTP requests"""
    try:
        response = requests.get(host)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False