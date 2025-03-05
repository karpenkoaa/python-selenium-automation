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
sleep(3)
driver.find_element(By. XPATH, "//a[@class='sc-a6f64ae6-1 sc-a6f64ae6-3 fKSfey erxjnr h-margin-l-wide']").click()
sleep(2)
driver.find_element(By. XPATH, "//span[@class='styles_wrapper__YYaWP' and text()='Home']").click()
driver.find_element(By. XPATH, "//*[text()='Furniture']")
