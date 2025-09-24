import time
from config.logger import get_logger
# from drivers.browsers import driver
from selenium.webdriver.common.by import By

log = get_logger()


def test_checkboxes(setup_browser):
    driver = setup_browser
    driver.get("https://the-internet.herokuapp.com/")
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/descendant::input[1]")
    assert checkbox1.is_displayed()
    checkbox1.click()
    checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/descendant::input[2]")
    assert checkbox2.is_displayed()
    checkbox2.click()
    time.sleep(2)
    driver.close()
