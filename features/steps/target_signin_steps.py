from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In in navigation menu')
def click_sign_in_button(context):
    context.app.headers.click_sign_in_nav_menu()
    sleep(3)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()
