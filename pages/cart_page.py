from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
   CART_MESSAGE_TEXT = (By. XPATH, "//h1[text()='Your cart is empty']")
   CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

   def verify_cart_message(self):
       self.verify_text('Your cart is empty', *self.CART_MESSAGE_TEXT)

   def verify_cart_page_opens(self):
       self.verify_url(f'{self.base_url}cart')

   def verify_items_in_cart(self, amount):
       self.driver.cart_summary = self.driver.find_element(*self.CART_SUMMARY).text
       assert f'{amount} item' in self.driver.cart_summary, f'Error. Expected {amount} items but got {self.driver.cart_summary}.'
