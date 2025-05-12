from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open Help page for returns')
def open_help_page_for_returns(context):
    context.app.help_page.open_help_returns()

@then('Verify help Returns page opens')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()

@when('Select help topic Gift Cards')
def select_topic(context):
    context.app.help_page.select_topic()

@then('Verify help Gift Cards opens')
def verify_gift_cards_opened(context):
    context.app.help_page.verify_gift_cards_opened()

