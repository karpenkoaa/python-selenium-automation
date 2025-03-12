from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By. XPATH, "//a[@class='sc-614114e5-1 sc-55744c41-0 kqKupI jPsZQE' and @aria-label='cart 0 items']").click()
    sleep(2)

@then('Verify correct message is shown')
def verify_correct_message(context):
    actual_text = context.driver.find_element(By. XPATH, "//h1[text()='Your cart is empty']")
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text.text, f'Error. Text {expected_text} is not in {actual_text}.'


