import logging

log = logging.getLogger(__name__)
class ClientLogger:

    @staticmethod
    def log_request(method, url, headers, **kwargs):
        log.info(f"Request method: {method}")
        log.info(f"URL: {url}")
        log.info(f"Headers: {headers}")
        if method in ['POST', 'PUT', 'PATCH']:
            log.info(f"Data: {kwargs.get('data')}")
            log.info(f"Json: {kwargs.get('json')}")
        if kwargs.get('params') is not None:
            log.info(f"Params: {kwargs.get('params')}")

    @staticmethod
    def log_response(response):
        log.info(f"Status: {response.status_code}")
        log.info(f"Response text: {response.text}")