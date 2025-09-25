import math
import time
import pytest

from selenium import webdriver

from config.logger import get_logger
from selenium.webdriver.common.by import By

log = get_logger()

@pytest.mark.usefixtures("setup_browser")
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


# single decorator
@pytest.mark.usefixtures("setup_browser")
@pytest.mark.parametrize("marks, total, result",
                         [
                             (350, 500, 70.00),
                             (400, 500, 80.00),
                             (450, 500, 90.00)
                         ])
def test_percentage(setup_browser, marks, total, result):
    driver = setup_browser
    driver.get("https://centrepointschools.com/calculator/percentage.html")
    driver.find_element(By.ID, 'number1').send_keys(marks)
    driver.find_element(By.ID, 'number2').send_keys(total)
    driver.find_element(By.XPATH, "//button[text()=' Calculate']").click()
    time.sleep(3)
    res = driver.find_element(By.XPATH, '//div[@id="txtHintCal"]//span  ')
    result_text = res.text
    print(f"Result_text : {result_text}")
    log.info(f"Result_text : {result_text}")
    # expected_text = f"Marks Percentage of  350 and 500 is 70.00"
    assert result == float(result_text)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()=' Clear']").click()


# Double decorator
@pytest.mark.parametrize("base", [1,2,3])
@pytest.mark.parametrize("exponent", [4,5,6])
def test_exponential(base, exponent):
    result = base**exponent
    assert math.pow(base, exponent) == result




