from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(4)

driver.find_element(By.ID, 'search').send_keys('chair')
sleep(2)
#optional test case
# Open https://www.target.com/
# Click Categories in nav bar
# Click Home
# MAke sure Furniture is shown in expanded home section

