from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_items_to_cart(self, *item_ids):
        for item_id in item_ids:
            locator = (By.ID, f"add-to-cart-{item_id}")
            self.driver.find_element(*locator).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
        return self

    def get_total_amount(self):
        footer = self.driver.find_element(By.CSS_SELECTOR, ".footer")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        return self.driver.find_element(*self.total_amount).text

def test_shopping_flow():
    service = Service(executable_path="C:/Users/anna.cherepanova/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=service) 
    
    try:
        page = LoginPage(driver).open()
        (page.login("standard_user", "secret_sauce")
            .add_items_to_cart("sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie")
            .go_to_cart()
            .proceed_to_checkout()
            .fill_shipping_info("Anna", "Cherepanova", "440000"))
        
        total = page.get_total_amount()
        expected_total = "Total: $58.29"
        assert total == expected_total, f"Error: expected '{expected_total}', got '{total}'"
    
    finally:
        driver.quit()