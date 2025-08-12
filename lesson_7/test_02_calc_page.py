from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")
        
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        return self
        
    def set_delay(self, seconds):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(seconds)
        return self
        
    def click_button(self, text):
        locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*locator).click()
        return self
        
    def get_result(self, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text

def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    
    try:
        calculator = CalculatorPage(driver)
        (calculator.open()
            .set_delay("45")
            .click_button("7")
            .click_button("+")
            .click_button("8")
            .click_button("="))
            
        result = calculator.get_result(46)
        assert result == "15", "Результат 15 не отобразился за 45 секунд"
    
    finally:
        driver.quit()