from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
   CART_MESSAGE_TEXT = (By. XPATH, "//h1[text()='Your cart is empty']")

   def verify_cart_message(self):
       actual_text = self.find_element(*self.CART_MESSAGE_TEXT).text
       expected_text = 'Your cart is empty'
       assert expected_text in actual_text, f'Error. Text {expected_text} is not in {actual_text}.'


