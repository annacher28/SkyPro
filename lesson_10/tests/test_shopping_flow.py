import allure
from ..pages.login_page import LoginPage


@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
class TestShoppingFlow:
    """Тесты для процесса покупки товаров."""
    
    @allure.title("Проверка полного процесса покупки товаров")
    @allure.description("""
    Тест проверяет полный процесс покупки:
    1. Авторизация пользователя
    2. Добавление товаров в корзину
    3. Переход в корзину
    4. Оформление заказа
    5. Проверка итоговой суммы
    """)
    def test_complete_shopping_flow(self, browser):
        """
        Тест полного процесса покупки товаров.
        
        Steps:
        1. Авторизоваться как standard_user
        2. Добавить три товара в корзину
        3. Перейти в корзину
        4. Перейти к оформлению заказа
        5. Заполнить информацию о доставке
        6. Проверить итоговую сумму заказа
        """
        with allure.step("Инициализация страницы авторизации"):
            login_page = LoginPage(browser).open()
        
        with allure.step("Авторизация пользователя"):
            inventory_page = login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Добавление товаров в корзину"):
            inventory_page.add_items_to_cart(
                "sauce-labs-backpack", 
                "sauce-labs-bolt-t-shirt", 
                "sauce-labs-onesie"
            )
        
        with allure.step("Переход в корзину"):
            cart_page = inventory_page.go_to_cart()
        
        with allure.step("Переход к оформлению заказа"):
            checkout_page = cart_page.proceed_to_checkout()
        
        with allure.step("Заполнение информации о доставке"):
            checkout_page.fill_shipping_info("Anna", "Cherepanova", "440000")
        
        with allure.step("Проверка итоговой суммы заказа"):
            total = checkout_page.get_total_amount()
            expected_total = "Total: $58.29"
            
            assert total == expected_total, (
                f"Ошибка: ожидалось '{expected_total}', получено '{total}'"
            )