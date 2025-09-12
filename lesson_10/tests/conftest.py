import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import allure


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и закрытия браузера.
    
    Yields:
        WebDriver: экземпляр WebDriver
    """
    service = Service(executable_path="C:/Users/anna.cherepanova/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    
    yield driver
    
    if driver:
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов.
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            if "browser" in item.funcargs:
                browser = item.funcargs["browser"]
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")