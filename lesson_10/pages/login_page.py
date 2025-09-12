from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .inventory_page import InventoryPage
import allure


class LoginPage:
    """Page Object для страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация LoginPage.

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.username_field = (By.XPATH, "//input[@placeholder='Username']")
        self.password_field = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: текущий экземпляр LoginPage
        """
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        return self

    @allure.step("Выполнить авторизацию с логином {username} и паролем {password}")
    def login(self, username: str, password: str) -> InventoryPage:
        """
        Выполняет авторизацию пользователя.

        Args:
            username: имя пользователя
            password: пароль пользователя

        Returns:
            InventoryPage: экземпляр страницы инвентаря
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver)