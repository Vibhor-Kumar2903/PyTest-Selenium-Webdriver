from pages.login_page import LoginPage
from tests_lambda.base_test import BaseTest
from utilities.test_data import TestData


class TestLogin(BaseTest):

    def test_valid_credential(self):
        login_page = LoginPage(self.driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_on_button()
        actual_title = login_page.get_title()
        assert actual_title == "My Account"