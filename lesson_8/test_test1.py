import requests

BASE_URL = "https://ru.yougile.com/api-v2/projects"
KEY = "AQGe8AOFoItt0VVs6FD0eeSupn9dHO0bJFS3Xx9L6YgJDCjIk-nVHre2N+92D0MS"
HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"}

def test_create_positive():
    payload = {"title": "Новый проект", "users": {"80bb24a0-f242-4500-955a-60b3da5660df": "admin"}}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    assert response.status_code == 201
    return response.json().get('id')

def test_get_positive():
    project_id = test_create_positive()
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200

def test_update_positive():
    project_id = test_create_positive()
    payload = {"deleted": True, "title": "ГосУслуги", "users": {"80bb24a0-f242-4500-955a-60b3da5660df": "admin"}}
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload, headers=HEADERS)
    assert response.status_code == 200

def test_create_negative():
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {KEY}"}
    payload = {"title": "Новый проект", "users": {"": "admin"}}
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 400

def test_get_negative():
    project_id = "test_id"
    response = requests.get(f"{BASE_URL}/{project_id}")
    assert response.status_code == 401

def test_update_negative():
    project_id = "test_id"
    payload = {"deleted": True, "users": {"80bb24a0-f242-4500-955a-60ba5660df": "admin"}}
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload)
    assert response.status_code == 401
