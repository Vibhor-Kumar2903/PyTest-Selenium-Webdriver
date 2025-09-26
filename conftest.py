import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

# from utilities.test_data import TestData


# 1st Step: Declare variable for setting up SwagLabs
username = 'standard_user'
password = 'secret_sauce'


# 2nd Step: Define the desire capabilities
chrome_caps = {
    "build": "1.0",
    "name": "Swag Labs grid on chrome",
    "platform": "windows 10",
    "browserName": "Chrome",
    "version": "latest"
}

firefox_caps = {
    "build": "2.0",
    "name": "Swag Labs grid on firefox",
    "platform": "windows 10",
    "browserName": "Firefox",
    "version": "latest"
}

edge_caps = {
    "build": "3.0",
    "name": "Swag Labs grid on edge",
    "platform": "windows 10",
    "browserName": "Edge",
    "version": "latest"
}


# 3rd Step: Connect to SwagLabs using a RemoteConnection
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
    # driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver ...")
    driver.close()








# log = get_logger()
#
# @pytest.fixture(autouse=True)
# def start_automatic_fixture():
#     log.info("==== START TESTING IN PYTEST FRAMEWORK ====")
#
# @pytest.fixture(scope="function")
# def setup_browser():
#     from selenium.webdriver.chrome.service import Service
#     from selenium.webdriver.chrome.options import Options
#     chrome_option = Options()
#     # It will keep open the browser after test execution
#     chrome_option.add_experimental_option('detach', True)
#     # It will ignore the internal background calls and noise which is not from selenium
#     chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
#     driver.maximize_window()
#     log.info("\nSetup, launching chrome browser...")
#     yield driver
#
#     log.info("\nTeardown, closing chrome browser...")
#     driver.quit()

# @pytest.fixture(scope="function")
#
# def teardown():
#     pass
