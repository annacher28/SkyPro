from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


service = Service(executable_path="C:/Users/anna.cherepanova/Documents/Драйвера/Driver_Notes/msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.XPATH, "//input[@name='first-name']")
first_name.click()
first_name.send_keys("Иван")

last_name = driver.find_element(By.XPATH, "//input[@name='last-name']")
last_name.click()
last_name.send_keys("Петров")

address = driver.find_element(By.XPATH, "//input[@name='address']")
address.click()
address.send_keys("Ленина, 55-3")

mail = driver.find_element(By.XPATH, "//input[@name='e-mail']")
mail.click()
mail.send_keys("test@skypro.com")

phone = driver.find_element(By.XPATH, "//input[@name='phone']")
phone.click()
phone.send_keys("+7985899998787")

city = driver.find_element(By.XPATH, "//input[@name='city']")
city.click()
city.send_keys("Москва")

country = driver.find_element(By.XPATH, "//input[@name='country']")
country.click()
country.send_keys("Россия")

job_position = driver.find_element(By.XPATH, "//input[@name='job-position']")
job_position.click()
job_position.send_keys("QA")

company = driver.find_element(By.XPATH, "//input[@name='company']")
company.click()
company.send_keys("SkyPro")


driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, ".alert-danger").value_of_css_property("border-color") == "rgb(245, 194, 199)"
)

WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, ".alert-success").value_of_css_property("border-color") == "rgb(186, 219, 204)"
)

print("Все проверки пройдены успешно!")



driver.quit()