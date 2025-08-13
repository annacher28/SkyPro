from selenium.webdriver.common.by import By
from .cart_page import CartPage

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