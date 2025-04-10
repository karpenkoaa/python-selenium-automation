from selenium.webdriver.common.by import By
from pages.base_page import Page

class Headers(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self):
        self.input_text('tea', *self.SEARCH_INPUT)
        self.click(*self.SEARCH_SUBMIT)



