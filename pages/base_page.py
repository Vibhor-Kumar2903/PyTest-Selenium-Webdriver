from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    """
    The purpose of a base page in to contain methods common to all page objects.
    """
    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def find(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()
        # self.driver.find_elements(*locator).click()

    def set(self, locator, value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_text(self,locator):
        return self.find(locator).text

    def get_title(self):
        return self.driver.title

    def pages(self, page_name):
        return By.XPATH, "//aside[@id='column-right']//a[contains(text(), '"+page_name+"')]"

    def click_on_menu_page(self, page_name):
        page = self.pages(page_name)
        self.click(page)

