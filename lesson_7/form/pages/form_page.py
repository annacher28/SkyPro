from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class FormPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.FIRST_NAME = (By.XPATH, "//input[@name='first-name']")
        self.LAST_NAME = (By.XPATH, "//input[@name='last-name']")
        self.ADDRESS = (By.XPATH, "//input[@name='address']")
        self.EMAIL = (By.XPATH, "//input[@name='e-mail']")
        self.PHONE = (By.XPATH, "//input[@name='phone']")
        self.CITY = (By.XPATH, "//input[@name='city']")
        self.COUNTRY = (By.XPATH, "//input[@name='country']")
        self.JOB_POSITION = (By.XPATH, "//input[@name='job-position']")
        self.COMPANY = (By.XPATH, "//input[@name='company']")
        self.SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
        self.DANGER_ALERT = (By.CSS_SELECTOR, ".alert-danger")
        self.SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()
        return self

    def fill_form(self, data: dict):
        self._fill_field(self.FIRST_NAME, data.get('first_name'))
        self._fill_field(self.LAST_NAME, data.get('last_name'))
        self._fill_field(self.ADDRESS, data.get('address'))
        self._fill_field(self.EMAIL, data.get('email'))
        self._fill_field(self.PHONE, data.get('phone'))
        self._fill_field(self.CITY, data.get('city'))
        self._fill_field(self.COUNTRY, data.get('country'))
        self._fill_field(self.JOB_POSITION, data.get('job_position'))
        self._fill_field(self.COMPANY, data.get('company'))
        return self

    def _fill_field(self, locator, text):
        if text:
            element = self.driver.find_element(*locator)
            element.click()
            element.clear()
            element.send_keys(text)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def wait_for_alerts(self):
        self.wait.until(
            lambda d: d.find_element(*self.DANGER_ALERT).value_of_css_property("border-color") == "rgb(245, 194, 199)"
        )
        self.wait.until(
            lambda d: d.find_element(*self.SUCCESS_ALERT).value_of_css_property("border-color") == "rgb(186, 219, 204)"
        )
        return self

    def are_alerts_displayed(self):
        return (
            self.driver.find_element(*self.DANGER_ALERT).is_displayed() and
            self.driver.find_element(*self.SUCCESS_ALERT).is_displayed()
        )