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

driver.find_element(By. XPATH, "//a[@class='sc-614114e5-1 sc-55744c41-0 kqKupI jPsZQE' and @aria-label='cart 0 items']").click()
sleep(2)
driver.find_element(By. XPATH, "//h1[text()='Your cart is empty']")
sleep(2)