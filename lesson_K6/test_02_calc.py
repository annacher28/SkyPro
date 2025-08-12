from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()

        element = driver.find_element(By.ID, "delay")
        element.clear()
        element.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result = WebDriverWait(driver, 46).until( 
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        assert result, "Результат 15 не отобразился за 45 секунд"
    
    finally:
        driver.quit()