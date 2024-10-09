import logging

import requests
from retrying import retry
from rest_client.client_logger import ClientLogger


class APIClient:
    def __init__(self, url = None, auth_handler = None, config = None):
        self.url = url
        self.auth_handler = auth_handler
        self.config = config

    @retry(wait_fixed=2000, stop_max_attempt_number=3)
    def _make_request(self, method, **kwargs):

        headers = self.config.merge_headers(self.auth_handler.headers) if self.auth_handler else self.config
        ClientLogger.log_request(method, self.url, headers, **kwargs)
        response = requests.request(method, self.url, headers=headers, **kwargs)
        ClientLogger.log_response(response)
        return self._handle_response(response)

    def _handle_response(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            raise
        except Exception as err:
            logging.error(f"Other error occurred: {err}")
            raise
        return response

    def get(self, params = None):
        return self._make_request('GET', params=params)

    def post(self, data = None, json = None):
        return self._make_request('POST', data=data, json=json)

    def put(self, data = None):
        return self._make_request('PUT', data=data)

    def patch(self, data = None):
        return self._make_request('PATCH', data=data)

    def delete(self, data = None):
        return self._make_request('DELETE', data=data)




