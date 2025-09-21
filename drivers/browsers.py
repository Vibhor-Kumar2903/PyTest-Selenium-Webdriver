from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
chrome_driver.maximize_window()


from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
edge_option = Options()
edge_option.add_experimental_option('detach', True)
edge_driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)
edge_driver.maximize_window()
