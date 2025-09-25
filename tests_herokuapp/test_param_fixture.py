import pytest
from selenium import webdriver


# Fixture param
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
    driver.close()


@pytest.mark.usefixtures("initialization_driver")
class BaseClass:
    pass

class Test_Driver(BaseClass):
    def test_multiple_browser(self):
        self.driver.get("https://centrepointschools.com/calculator/percentage.html")
        page_title = self.driver.title
        assert page_title == "Online Percentage Calculator | Centre Point School"


