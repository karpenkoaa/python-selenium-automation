from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    USER_NAME_FIELD = (By.ID, 'username')
    CONTINUE_BTN = (By.ID, 'login')
    SIGN_IN_W_PSWD_BTN = (By.ID, 'login')
    ERR_MSG = (By.ID, 'password--ErrorMessage')


    def verify_sign_in(self):
        self.verify_text('Sign in or create account', *self.SIGN_IN_PAGE_TEXT)

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('target.com/c/terms-conditions')

    def enter_email_address(self):
        self.input_text(*self.USER_NAME_FIELD).send_keys('karpenkoalina1295@gmail.com')

    def click_signin_with_password(self):
        self.click(*self.SIGN_IN_W_PSWD_BTN)

    def verify_error_message(self):
        self.verify_partial_text('Please enter your password', *self.ERR_MSG)


