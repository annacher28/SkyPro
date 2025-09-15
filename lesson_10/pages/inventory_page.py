from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .cart_page import CartPage
import allure


class InventoryPage:
    """Page Object для страницы инвентаря товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация InventoryPage.

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Добавить товары в корзину: {item_ids}")
    def add_items_to_cart(self, *item_ids: str) -> 'InventoryPage':
        """
        Добавляет товары в корзину по их идентификаторам.

        Args:
            *item_ids: идентификаторы товаров для добавления

        Returns:
            InventoryPage: текущий экземпляр InventoryPage
        """
        for item_id in item_ids:
            locator = (By.ID, f"add-to-cart-{item_id}")
            self.driver.find_element(*locator).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.

        Returns:
            CartPage: экземпляр страницы корзины
        """
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)