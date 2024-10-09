
class RequestConfig:
    def __init__(self, headers=None, timeout=10, retries=3):
        self.headers = headers
        self.timeout = timeout
        self.retries = retries

    def merge_headers(self, auth_headers):
        combined_headers = {**self.headers, **auth_headers}
        return combined_headers