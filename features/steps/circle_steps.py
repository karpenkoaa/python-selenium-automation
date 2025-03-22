from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, ".cell-item-content")

@given('Open target circle page')
def open_target_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)

@then('Verify benefit cells')
def verify_benefit(context):
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(cells)
    assert len(cells) >= 10, f'Expected 10 cells, got {len(cells)}'
