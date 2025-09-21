import time
from config.logger import get_logger
from drivers.browsers import chrome_driver

log = get_logger()

def test_herokuapp_title():
    chrome_driver.get("https://the-internet.herokuapp.com/")
    log.info(f"Page Title : {chrome_driver.title}")
    time.sleep(2)
    chrome_driver.close()

