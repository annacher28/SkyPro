from selenium.webdriver.common.by import By
from .inventory_page import InventoryPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@placeholder='Username']")
        self.password_field = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        return self

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver)