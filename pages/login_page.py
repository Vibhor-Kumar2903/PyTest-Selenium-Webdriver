from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    email_textbox = (By.ID, 'input-email')
    password_textbox = (By.ID, 'input-password')
    login_button = (By.XPATH, '//input[@value="Login"]')
    warning_msg = (By.CSS_SELECTOR, 'div.alert alert-danger alert-dismissible')


    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(self.email_textbox, email_address)
        # self.driver.find_element(self.email_textbox).send_keys(email_address)

    def set_password(self, password):
        self.set(self.password_textbox, password)

    def click_on_button(self):
        self.click(self.login_button)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_on_button()

    def get_warning_msg(self):
        return self.get_text(self.warning_msg)

    # def get_confirmation_msg(self):
    #     return self.get_text(self.confirmation_msg)