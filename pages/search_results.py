from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResults(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_result_text(self):
        actual_text = self.find_element(*self.SEARCH_RESULT_TEXT).text
        assert 'tea' in actual_text, f'Error tea not in {actual_text}'
