from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&ignoreAuthState=1&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&disableLoginPrepopulate=1&switch_account=signin&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(2)

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @role='presentation']")
driver.find_element(By.CSS_SELECTOR,".a-spacing-small")
driver.find_element(By.XPATH, "//input[@id='ap_customer_name' and @class='a-input-text a-span12 auth-autofocus auth-required-field']")
driver.find_element(By.CSS_SELECTOR, "input#ap_email.a-input-text a-span12 auth-required-field auth-require-claim-validation")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

