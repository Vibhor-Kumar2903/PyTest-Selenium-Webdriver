import time
from config.logger import get_logger
# from drivers.browsers import driver
from selenium.webdriver.common.by import By

log = get_logger()

def test_herokuapp_title(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    log.info(f"Page Title : {driver.title}")
    time.sleep(3)
    driver.close()


def test_add_element(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    log.info(f"Page Title : {driver.title}")
    time.sleep(3)
    driver.close()


