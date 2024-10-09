import pytest
import logging

from utils import pet_utils
from utils.config_parser import get_pet_app_url

base_url = get_pet_app_url()
log = logging.getLogger(__name__)

def get_all_status():
    return ["available", "pending", "sold"]

class TestPetAPIS:

    @pytest.mark.parametrize("status", get_all_status())
    def test_get_pets(self, status):
        log.info(f"Starting test_get_pets with status {status}")
        response = pet_utils.get_pets_with_status(base_url + "/findByStatus", status)
        assert response.status_code == 200
        log.info(f"completed test_get_pets with status {status}")


    def test_create_pet(self, get_create_pet_json):
        payload = get_create_pet_json
        response = pet_utils.create_pet(base_url, payload)
        assert response.status_code == 200


