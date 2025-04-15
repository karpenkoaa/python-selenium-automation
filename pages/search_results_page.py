from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_result_text(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULT_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

