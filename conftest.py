import os
import sys

import pytest
import logging


@pytest.fixture(scope='function', autouse=True)
def log_each_test(request):
    test_name = request.node.name
    module_name = request.module.__name__
    log_dir = os.path.join('log', module_name)
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, '{}.log'.format(test_name))

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    file_handler = logging.FileHandler(log_file, mode='w')
    formatter = logging.Formatter('%(asctime)s [%(levelname)8s] %(name)s %(message)s (%(filename)s:%(lineno)s)',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # Store the handler to remove it later
    request.node._handler = file_handler

    yield
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    file_handler.close()




