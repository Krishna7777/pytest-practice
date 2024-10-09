import logging
import time

log = logging.getLogger(__name__)

def poll_until(func, timeout = 60, interval = 5, *args, **kwargs):
    start_time = time.time()
    end_time = start_time + timeout
    while time.time() < end_time:
        if func(*args, **kwargs):
            return True
        log.info(f"retrying again after {timeout} seconds")
        time.sleep(interval)
    return False
