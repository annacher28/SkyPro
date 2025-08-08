from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()
waiter = WebDriverWait(driver, 40)


waiter.until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

third_img = driver.find_elements(By.CSS_SELECTOR, "#image-container img")[2]
print(third_img.get_attribute("src"))


sleep(2)  
driver.quit()