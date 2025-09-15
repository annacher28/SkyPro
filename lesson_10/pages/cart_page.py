from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .checkout_page import CheckoutPage
import allure


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация CartPage.

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self) -> CheckoutPage:
        """
        Переходит к оформлению заказа.

        Returns:
            CheckoutPage: экземпляр страницы оформления заказа
        """
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)