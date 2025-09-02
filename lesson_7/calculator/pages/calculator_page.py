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