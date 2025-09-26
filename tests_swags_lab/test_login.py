import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from conftest import username, password

@pytest.fixture(params=["chrome","firefox","edge"])
def initialization_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver
    print(f"Browser : {request.param}")
    yield
    print("Close Driver ...")
    driver.quit()


@pytest.mark.usefixtures("initialization_driver")
class Test_Driver:
    def test_swag_login(self, initialization_driver):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()
        # self.driver.switch_to.alert.accept()



