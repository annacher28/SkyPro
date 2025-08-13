from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from lesson_7.shop.pages.login_page import LoginPage

def test_shopping_flow():
    service = Service(executable_path="C:/Users/anna.cherepanova/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    
    try:
        login_page = LoginPage(driver).open()
        inventory_page = login_page.login("standard_user", "secret_sauce")
        inventory_page.add_items_to_cart("sauce-labs-backpack", 
                                      "sauce-labs-bolt-t-shirt", 
                                      "sauce-labs-onesie")
        cart_page = inventory_page.go_to_cart()
        checkout_page = cart_page.proceed_to_checkout()
        checkout_page.fill_shipping_info("Anna", "Cherepanova", "440000")
        
        total = checkout_page.get_total_amount()
        expected_total = "Total: $58.29"
        assert total == expected_total, f"Ошибка: ожидалось '{expected_total}', получено '{total}'"
    
    finally:
        driver.quit()