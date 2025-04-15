from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
IDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton'][id*='addToCart']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

@then('Verify search worked for {expected_text}')
def verify_search_worked(context, expected_text):
    sleep(3)
    context.app.search_results_page.verify_search_result_text(expected_text)


@when('Click Add to cart on the product')
def click_add_to_cart(context):
    context.driver.execute_script("window.scrollTo(0, 2300);")
    sleep(8)
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN))
    context.app.search_results_page.click_add_to_cart_btn()


@when ('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(IDE_NAV_ADD_TO_CART_BTN))
    context.app.headers.add_to_cart_nav_menu()

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)

@then('Product results are shown for {expected_result}')
def verify_found_results_text(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result in actual_text, \
        f'Expected query not in {actual_text}'

@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results_page.verify_results_url(expected_text)
