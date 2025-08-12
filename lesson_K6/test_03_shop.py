from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 


def test_shopping_cart():
    service = Service(executable_path="C:/Users/anna.cherepanova/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=service) 
    
    try:
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        username.click()
        username.send_keys("standard_user")

        Password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        Password.click()
        Password.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        first_name = driver.find_element(By.ID, "first-name")
        first_name.click()
        first_name.send_keys("Анна")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.click()
        last_name.send_keys("Черепанова")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.click()
        postal_code.send_keys("440000")

        driver.find_element(By.ID, "continue").click()

        footer = driver.find_element(By.CSS_SELECTOR, ".footer")
        driver.execute_script("arguments[0].scrollIntoView(true);", footer)

        total_label = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")

        label_text = total_label.text
        expected_text = "Total: $58.29"
        assert label_text == expected_text, f"Ошибка: ожидалось '{expected_text}', получено '{label_text}'"
    
    finally:
        driver.quit()