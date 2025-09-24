# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium import webdriver
#
#
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# chrome_option = Options()
# #It will keep open the browser after test execution
# chrome_option.add_experimental_option('detach', True)
# #It will ignore the internal background calls and noise which is not from selenium
# chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
# driver.maximize_window()


# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# firefox_option = Options()
# firefox_option.set_preference('detach', True)
# driver = webdriver.Chrome(service=Service(GeckoDriverManager().install()), options=chrome_option)
# driver.maximize_window()


# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# edge_option = Options()
# edge_option.add_experimental_option('detach', True)
# driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)
# driver.maximize_window()

