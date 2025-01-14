import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если прочитанная строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Замените на реальные названия файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов: {linear_duration:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool(processes=4) as pool:  # Укажите количество процессов, которое хотите использовать
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocessing_duration:.6f} секунд")