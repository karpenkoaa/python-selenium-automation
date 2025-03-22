from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(6)


@then('Product results are shown for {expected_result}')
def verify_found_results_text(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result in actual_text, \
        f'Expected query not in {actual_text}'
