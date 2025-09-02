import requests

class CompanyApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_company_list(self, params_to_add=None):
        # URL для получения списка компаний
        url = f"{self.base_url}/companies"
        
        # Отправляем GET-запрос к API
        response = requests.get(url, params=params_to_add)
        
        # Проверяем, что запрос успешен
        if response.status_code == 200:
            return response.json()  # Возвращаем данные в формате JSON
        else:
            response.raise_for_status()  # Вызываем ошибку, если что-то пошло не так