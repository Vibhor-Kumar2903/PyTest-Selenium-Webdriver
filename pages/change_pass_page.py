from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage
from utilities.locators import ChangePasswordLocators

class ChangePasswordPage(BasePage, ChangePasswordLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.locate = ChangePasswordLocators

    def change_password(self, password, confirm_password):
        self.set(self.locate.password_textbox, password)
        self.set(self.locate.confirm_password_textbox, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)

    def get_confirmation_error_message(self):
        return self.get_text(self.locate.confirmation_msg)

    

















