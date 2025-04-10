from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)

@then('Verify user can click through colors')
def verify_user_colors(context):
    expected_colors = ['beige', 'brown']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
       color.click()

       selected_color = context. driver.find_element(*SELECTED_COLOR).text
       print('Current color', selected_color)

       selected_color = selected_color.split('\n')[1]
       actual_colors.append(selected_color)
       print(actual_colors)

    assert actual_colors == expected_colors, f'Expected colors: {expected_colors} did not match Actual colors: {actual_colors}'


