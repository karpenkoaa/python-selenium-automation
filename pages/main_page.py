from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
   CART_BUTTON = (By.XPATH, "//a[@class='sc-614114e5-1 sc-55744c41-0 kqKupI jPsZQE' and @aria-label='cart 0 items']")
   SEARCH_INPUT = (By.ID, 'search')
   SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

   def open_main_page(self):
       self.open_url('https://www.target.com/')
       self.wait_until_visible(*self.SEARCH_INPUT)

   def click_cart_btn(self):
       self.click(*self.CART_BUTTON)

   def click_search_btn(self):
        self.click(*self.SEARCH_SUBMIT)


