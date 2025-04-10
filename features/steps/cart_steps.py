from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-linked-title']")

@when('Open cart Page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')

@then('Verify correct message is shown')
def verify_correct_message(context):
    context.app.cart_page.verify_cart_message()

@then('Verify Cart has {amount} item(s)')
def verify_cart_has_one_items(context, amount):
    context.driver.wait.until(EC.presence_of_element_located(CART_SUMMARY))
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f'Error. Expected {amount} items but got {cart_summary}.'


@then('Verify cart has correct product')
def verify_product_name(context):
    context.driver.wait.until(EC.text_to_be_present_in_element(CART_ITEM_TITLE))
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == product_name_in_cart, f'Error'
