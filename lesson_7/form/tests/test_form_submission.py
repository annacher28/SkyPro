from selenium import webdriver
from selenium.webdriver.edge.service import Service
from ..pages.form_page import FormPage

def test_form_submission():
    service = Service(executable_path="C:/Users/anna.cherepanova/Documents/Драйвера/Driver_Notes/msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    try:
        form_data = {
            'first_name': 'Иван',
            'last_name': 'Петров',
            'address': 'Ленина, 55-3',
            'email': 'test@skypro.com',
            'phone': '+7985899998787',
            'city': 'Москва',
            'country': 'Россия',
            'job_position': 'QA',
            'company': 'SkyPro'
        }

        form_page = FormPage(driver).open()
        (form_page.fill_form(form_data)
                .submit()
                .wait_for_alerts())

        assert form_page.are_alerts_displayed(), "Не все элементы отображаются корректно"
        
    finally:
        driver.quit()