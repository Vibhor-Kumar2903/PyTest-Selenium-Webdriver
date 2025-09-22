import time
from config.logger import get_logger
from drivers.browsers import driver
from selenium.webdriver.common.by import By

log = get_logger()

def test_add_and_remove_element():
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    log.info(f"Page Title : {driver.title}")
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    time.sleep(2)
    driver.close()