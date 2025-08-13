from selenium.webdriver.common.by import By
from .checkout_page import CheckoutPage

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)