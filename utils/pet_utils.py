from charset_normalizer.cli import cli_detect

from rest_client.APIClient import APIClient
from utils.config_parser import get_pet_app_url

base_url = get_pet_app_url()


def get_pets_with_status(url, status):
    header = {"Content-Type": "application/json"}
    client = APIClient(url, None, header)
    params = {"status": status}
    response = client.get(params=params)
    return response

def create_pet(url, payload, op_headers=None):
    header = {"Content-Type": "application/json"}
    header = {header | op_headers} if isinstance(op_headers, dict) else header
    client = APIClient(url, None, header)
    response = client.post(json=payload)
    return response

