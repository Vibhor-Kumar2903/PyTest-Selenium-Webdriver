import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from config.logger import get_logger

log = get_logger()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    log.info("==== START TESTING IN PYTEST FRAMEWORK ====")

@pytest.fixture(scope="function")
def setup_browser():
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    chrome_option = Options()
    # It will keep open the browser after test execution
    chrome_option.add_experimental_option('detach', True)
    # It will ignore the internal background calls and noise which is not from selenium
    chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    driver.maximize_window()
    log.info("\nSetup, launching chrome browser...")
    yield driver

    log.info("\nTeardown, closing chrome browser...")
    driver.quit()

# @pytest.fixture(scope="function")
#
# def teardown():
#     pass
