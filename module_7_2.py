def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}

        for i, string in enumerate(strings):
            start_byte = file.tell()  # Получаем текущее положение в байтах
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i + 1, start_byte)] = string  # Сохраняем в словарь

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
