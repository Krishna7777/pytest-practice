import pytest
import logging

from utils.file_utils import get_json_from_file
log = logging.getLogger()

@pytest.fixture()
def get_create_pet_json():
    create_json = get_json_from_file("pet_api_json","create_pet.json")
    return create_json

@pytest.fixture(scope="class", autouse=True)
def setup_and_teardown_class_fixture(request):
    class_name = request.cls.__name__
    log.info(f"Starting setup class of {class_name}")
    yield
    log.info(f"Completed teardown class of {class_name}")


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_fixture(request):
    class_name = request.cls.__name__
    log.info(f"Starting setup of {class_name}")
    yield
    log.info(f"Completed teardown of {class_name}")
