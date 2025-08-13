from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from lesson_7.calculator.pages.calculator_page import CalculatorPage  # Абсолютный импорт

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