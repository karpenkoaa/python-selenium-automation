from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(4)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(2)

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By. XPATH, "//a[@class='sc-614114e5-1 sc-55744c41-0 kqKupI jPsZQE' and @aria-label='cart 0 items']").click()
    sleep(2)

@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test=@web/Search/SearchButton']").click()
    sleep(2)

@when('Click view cart')
def click_view_cart(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']")
    sleep(4)


