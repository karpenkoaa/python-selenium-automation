from pages.base_page import Page
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.headers import Headers
from pages.search_results_page import SearchResults
from pages.sign_in_page import SignInPage
from pages.help_page import HelpPage

class Application:
    def __init__ (self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.base_page = Page(driver)
        self.headers = Headers(driver)
        self.search_results_page = SearchResults(driver)
        self.sign_in_page = SignInPage(driver)
        self.help_page = HelpPage(driver)

