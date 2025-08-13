import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def browser():
    service = Service(executable_path="C:/Users/anna.cherepanova/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()