import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import allure
import os


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и закрытия браузера.
    
    Yields:
        WebDriver: экземпляр WebDriver
    """

    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    driver.maximize_window()
    
    yield driver
    
    if driver:
        driver.quit()


@pytest.fixture
def browser_headless():
    """
    Фикстура для запуска браузера в headless-режиме.
    """
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    yield driver
    
    if driver:
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов.
    
    Args:
        item: объект теста
        call: информация о вызове теста (setup, call, teardown)
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:

            browser_obj = item.funcargs.get("browser")
            if browser_obj:

                allure.attach(
                    browser_obj.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
                print("Скриншот при падении теста сохранен в отчет Allure")
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")


@pytest.fixture
def test_data_path():
    """
    Фикстура для получения пути к тестовым данным.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "test_data")