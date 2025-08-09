from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
element = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
print(element.text)


driver.quit()