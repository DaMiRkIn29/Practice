import requests

# Удаление первого пользователя
response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
if response.status_code in [200, 204]:
    print("Пользователь успешно удален.")
else:
    print(f"Ошибка при удалении пользователя: {response.status_code}")

new_user = {
    'name': 'Новый пользователь',
    'username': 'новый_юзер',
    'email': 'novyy_user@example.com',
    'address': {
        'street': 'Улица 1',
        'suite': 'Квартира 1',
        'city': 'Город',
        'zipcode': '12345',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    },
    'phone': '1-770-736-8031 x56442',
    'website': 'novyy_user.com',
    'company': {
        'name': 'Компания',
        'catchPhrase': 'Уникальный слоган',
        'bs': 'бизнес-слоган'
    }
}

response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user)
if response.status_code == 201:
    print("Новый пользователь успешно создан!")
    print(response.json())
else:
    print(f"Ошибка при создании пользователя: {response.status_code}")

# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/users')
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")

# Параметры для GET-запроса
params = {
    'username': 'новый_юзер'
}

# Отправляем GET-запрос для получения пользователей по параметру
response = requests.get('https://jsonplaceholder.typicode.com/users', params=params)
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")