from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SIGN_IN_BTN = (By.CSS_SELECTOR, "#account-sign-in")
SIGN_IN_BTN_NAV = (By.XPATH, "//button[@data-test='accountNav-signIn']")


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.main_page.open_main_page()
    context.app.base_page.wait_until_clickable(*SIGN_IN_BTN)
    context.app.base_page.wait_until_clickable(*SIGN_IN_BTN_NAV)


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_tc_link()

@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_is_opened(context):
    context.app.sign_in_page.verify_tc_opened()

@then('Close new window')
def close_new_window(context):
    context.app.base_page.close()

@then('Switch back to original window')
def switch_to_back_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)

