
import requests


def is_host_http_ok(host: str, expect_status=200) -> bool:
    """Check if the host is up and responding to HTTP requests"""
    try:
        response = requests.get(host)
        print(f"HTTP response: {response.status_code}")
        return response.status_code == expect_status
    except requests.exceptions.ConnectionError:
        return False
