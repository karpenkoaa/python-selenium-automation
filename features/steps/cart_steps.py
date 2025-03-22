from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify correct message is shown')
def verify_correct_message(context):
    actual_text = context.driver.find_element(By. XPATH, "//h1[text()='Your cart is empty']")
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text.text, f'Error. Text {expected_text} is not in {actual_text}.'


@then('Product added to the cart')
def product_added(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']")
    expected_text = 'Added to cart'
    assert expected_text == actual_text.text, f'Error. Text {expected_text} is not in {actual_text}'


