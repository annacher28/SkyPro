from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="C:/Документы/браузеры/geckodriver-v0.36.0-win64/geckodriver.exe")
driver = webdriver.Firefox(service=service) 
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
)
input_field.send_keys("Sky") 
sleep(2)

input_field.clear()
input_field.send_keys("Pro") 

sleep(2)
driver.quit()