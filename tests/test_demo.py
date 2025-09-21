from drivers.browsers import chrome_driver

def test_lambdatest_playground():
    chrome_driver.get("https://www.lambdatest.com/selenium-playground/")
    print(f"Page Title : {chrome_driver.title}")