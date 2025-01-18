import requests

# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print(response.json())  # Выводим данные в формате JSON
else:
    print(f"Ошибка: {response.status_code}")

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Проверяем статус-код ответа
if response.status_code == 201:
    print("Данные успешно отправлены!")
    print(response.json())  # Выводим ответ сервера
else:
    print(f"Ошибка: {response.status_code}")

# Параметры для запроса
params = {
    'userId': 1
}

# Отправляем GET-запрос с параметрами
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Проверяем статус-код ответа
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print(response.json())  # Выводим данные в формате JSON
else:
    print(f"Ошибка: {response.status_code}")