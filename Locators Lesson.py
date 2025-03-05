from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(4)

driver.find_element(By.CLASS_NAME, 'a-icon a-icon-logo')
driver.find_element(By.XPATH, "//input[@id='continue']")
driver.find_element(By.NAME, 'email')
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//h5[text()='New to Amazon?']")
driver.find_elements(By. XPATH, "//span[@class='a-text-bold']" )
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit' and @class='a-button-text']"))

#target test

driver.get('https://www.target.com/')
driver.find_element(By. XPATH, "//span[@class='sc-58ad44c0-3 cOUViz h-margin-r-x3']").click()
sleep(5)
driver.find_element(By. XPATH, "//button[@class='styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH h-margin-t-x2 h-margin-b-default']").click()
sleep(5)
driver.find_element(By. XPATH, "//span[text()='Sign into your Target account']")

print(f'Test case Passed')

#optional test case
# Open https://www.target.com/
# Click Categories in nav bar
# Click Home
# MAke sure Furniture is shown in expanded home section

driver.get('https://www.target.com/')
sleep(3)
driver.find_element(By. XPATH, "//a[@class='sc-a6f64ae6-1 sc-a6f64ae6-3 fKSfey erxjnr h-margin-l-wide']").click()
sleep(2)
driver.find_element(By. XPATH, "//span[@class='styles_wrapper__YYaWP' and text()='Home']").click()
driver.find_element(By. XPATH, "//*[text()='Furniture']")