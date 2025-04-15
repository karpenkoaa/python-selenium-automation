from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, 'search')
SEARCH_SUBMIT = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
IDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test=''content-wrapper'][id*='addToCart']")

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)

@when('Click on search icon')
def click_search_icon(context):
    context.app.main_page.click_search_btn()






