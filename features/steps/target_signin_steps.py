from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(2)

@when('Click Sign In in navigation menu')
def click_sign_in_button(context):
    context.driver.find_element(By. XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH h-margin-t-x2 h-margin-b-default']").click()
    sleep(2)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text = context.driver.find_element(By. XPATH, "//span[text()='Sign into your Target account']")
    expected_text = 'Sign into your Target account'
    assert expected_text in actual_text.text, f'Error. Text {expected_text} is not in {actual_text}.'
