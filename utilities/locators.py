from selenium.webdriver.common.by import By

class ChangePasswordLocators:
    password_textbox = (By.ID, 'input-password')
    confirm_password_textbox = (By.ID, 'input-confirm')
    continue_button = (By.XPATH, '//input[@value="Continue"]')
    not_match_msg = (By.CLASS_NAME, 'text-danger') #get its text
    confirmation_msg = (By.CLASS_NAME, 'alert alert-success alert-dismissible') #get its text




