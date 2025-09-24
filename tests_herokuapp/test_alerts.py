import time
import pytest

from config.logger import get_logger
# from drivers.browsers import driver
from selenium.webdriver.common.by import By

log = get_logger()

@pytest.mark.smoke
def test_basic_auth_alert(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Basic Auth").click()
    username = "admin"
    password = "admin"
    url = "https://the-internet.herokuapp.com/basic_auth"
    driver.get(f"https://{username}:{password}@{url}")
    time.sleep(5)
    basic_auth = driver.find_element(By.XPATH, "//div[@id='content']//h3[contains(text(), 'Basic Auth')]")
    basic_auth.is_displayed()
    log.info("Logged in successfully")

@pytest.mark.regression
@pytest.mark.integration
def test_checkboxes(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    log.info(f"landing page : {driver.title}")
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    log.info(f"Checkbox page : {driver.title}")
    checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/descendant::input[1]")
    assert checkbox1.is_displayed()
    checkbox1.click()
    checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/descendant::input[2]")
    assert checkbox2.is_displayed()
    checkbox2.click()
    time.sleep(2)
    driver.close()

