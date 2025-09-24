import time
import pytest
from config.logger import get_logger
from selenium.webdriver.common.by import By

@pytest.fixture()
@pytest.mark.parametrize("name",
                         [
                             ("Vibhor"),
                             ("Naina"),
                             ("Vedansh")
                         ])

def test_fill_the_form(setup_browser, name):
    driver = setup_browser
    driver.get("https://demoqa.com/")
    driver.find_element(By.XPATH, "//div[@class='home-body']//div[2]//div[1]//div[2]//*[name()='svg']").click()
    driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()
    name_textbox = driver.find_element(By.XPATH, "//input[@id='firstName']")
    name_textbox.send_keys(name)
    time.sleep(3)
    name_textbox.clear()



