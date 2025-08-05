from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path="C:/Документы/браузеры/geckodriver-v0.36.0-win64/geckodriver.exe")
driver = webdriver.Firefox(service=service)  
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")


input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
)
input_field.send_keys("tomsmith") 

input_field2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
)
input_field2.send_keys("SuperSecretPassword!") 

input_field3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']"))
) 
input_field3.click()

print("You logged into a secure area!")

sleep(2)
driver.quit()