import requests

key ="Подставить"
Base_url = "https://ru.yougile.com/api-v2/projects"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

#Позитивные проверки
#1
payload = {
    "title": "Новый проект",
    "users": {"80bb24a0-f242-4500-955a-60b3da5660df": "admin"}
}

response = requests.request("POST", Base_url, json=payload, headers=headers)

print(response.text)

assert response.status_code == 201

#2
response = requests.request("GET", Base_url + '/4cbb973c-7340-443d-a0d0-08c591da42ae', headers=headers)

print(response.text)

assert response.status_code == 200

#3
payload = {
    "deleted": True,
    "title": "ГосУслуги",
    "users": {"80bb24a0-f242-4500-955a-60b3da5660df": "admin"}
}

response = requests.request("PUT", Base_url + '/a70f69b6-a7bb-47a4-b10d-b0d33c12903b', json=payload, headers=headers)

print(response.text)

assert response.status_code == 200

#Негативные проверки
#1
response = requests.request("POST", Base_url, json=payload, headers=headers)

print(response.text)

assert response.status_code == 400
#2
headers = {
    "Content-Type": "application/json"
}

response = requests.request("GET", Base_url + '/a70f69b6-a7bb-47a4-b10d-b0d33c12903b', headers=headers)

print(response.text)

assert response.status_code == 401
#3
payload = {
    "deleted": True,
    "users": {"80bb24a0-f242-4500-955a-60ba5660df": "admin"}
}
headers = {
    "Authorization": f"Bearer {key}"
}

response = requests.request("PUT", Base_url + '/a70f69b6-a7bb-47a4-b10d-b0d33c12903b')

print(response.text)

assert response.status_code == 401