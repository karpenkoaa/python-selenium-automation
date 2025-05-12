from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_PAGE_TEXT = (By.XPATH, "//h1[text()='Sign in or create account']")
CONTINUE_BTN = (By.ID, 'login')
USER_NAME_FIELD = (By.ID, 'username')

@when('Click Sign In in navigation menu')
def click_sign_in_button(context):
    context.app.headers.click_sign_in_nav_menu()
    sleep(3)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()

@when('Enter correct email address and click continue')
def enter_email_and_click_continue(context):
    context.app.base_page.wait_until_visible(*USER_NAME_FIELD)
    context.app.base_page.input_text('karpenkoalina1295@gmail.com', *USER_NAME_FIELD)
    context.app.base_page.click(*CONTINUE_BTN)
    sleep(3)

@when('Click Sign In with password')
def click_sign_in_w_password(context):
    context.app.sign_in_page.click_signin_with_password()

@then('Verify error message is shown')
def verify_error_message(context):
    context.app.sign_in_page.verify_error_message()
