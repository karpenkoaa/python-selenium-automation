from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE_TEXT = (By. XPATH, "//h1[text()='Sign in or create account']")

    def verify_sign_in(self):
        self.verify_text('Sign in or create account', *self.SIGN_IN_PAGE_TEXT)