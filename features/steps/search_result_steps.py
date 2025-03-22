from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search worked for {expected_product}')
def verify_search_worked(context, expected_product):
    search_result_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test=@web/Search/SearchButton']").text
    assert expected_product in search_result_header, \
       f'Expected text {expected_product} not in {search_result_header}'


@when('Click Add to cart on the product')
def click_add_to_cart(context):
    context.driver.find_element(By.XPATH, "//div[@style='display: inline-block;']//button[@id='addToCartButtonOrTextIdFor93530117']").click()
    context.driver.find_element(By.XPATH, "//div[@style='display: flex;']//button[@id='addToCartButtonOrTextIdFor93530117']").click()