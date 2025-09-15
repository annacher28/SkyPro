from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация CheckoutPage.

        Args:
            driver: WebDriver экземпляр браузера
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CSS_SELECTOR, ".summary_total_label")

    @allure.step("Заполнить информацию о доставке: {first_name} {last_name}, {postal_code}")
    def fill_shipping_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """
        Заполняет информацию о доставке.

        Args:
            first_name: имя покупателя
            last_name: фамилия покупателя
            postal_code: почтовый индекс

        Returns:
            CheckoutPage: текущий экземпляр CheckoutPage
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
        return self

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: текст с итоговой суммой
        """
        footer = self.driver.find_element(By.CSS_SELECTOR, ".footer")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)
        return self.driver.find_element(*self.total_amount).text