from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
IDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton'][id*='addToCart']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()
    sleep(4)

@when('Click Sign In')
def click_sign_in(context):
    context.app.headers.click_sign_in()
    sleep(2)

@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_btn()
    sleep(2)

@when('Search for {expected_text}')
def search_for_product(context, expected_text):
    context.app.headers.search()

@when('Click view cart')
def click_view_cart(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']")
    sleep(4)


