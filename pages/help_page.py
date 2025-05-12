from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class HelpPage(Page):
    HEADERS_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    HEADERS_GIFT_CARDS = (By.XPATH, "//h1[text()=' Target GiftCard balance']")


    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_returns_opened(self):
        self.wait_until_visible(*self.HEADERS_RETURNS)

    def select_topic(self):
        dd = self.find_element(*self.TOPIC_SELECTION_DD)

        select = Select(dd)
        select.select_by_value('Gift Cards')

    def verify_gift_cards_opened(self):
        self.wait_until_visible(*self.HEADERS_GIFT_CARDS)


