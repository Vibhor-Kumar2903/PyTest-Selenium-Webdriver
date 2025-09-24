import time
import pytest

from config.logger import get_logger
from selenium.webdriver.common.by import By

log = get_logger()

@pytest.mark.integration
def test_add_and_remove_element(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    log.info(f"Page Title : {driver.title}")
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    time.sleep(2)
    driver.close()