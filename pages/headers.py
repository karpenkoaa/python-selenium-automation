from selenium.webdriver.common.by import By
from pages.base_page import Page

class Headers(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#account-sign-in")
    SIGN_IN_BTN_NAV = (By. XPATH, "//button[@data-test='accountNav-signIn']")
    IDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton'][id*='addToCart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def search(self):
        self.input_text('tea', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)

    def click_sign_in_nav_menu(self):
        self.click(*self.SIGN_IN_BTN_NAV)

    def add_to_cart_nav_menu(self):
        self.click(*self.IDE_NAV_ADD_TO_CART_BTN)




