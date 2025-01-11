import time
from threading import Thread, Lock  # Из-за некорректного вывода в консоль, решил воспользоваться Lock, не бейте


class Knight(Thread):
    def __init__(self, name, power, lock):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.lock = lock
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            remaining = max(self.enemies, 0)
            with self.lock:
                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining} воинов.")

        with self.lock:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


lock = Lock()

first_knight = Knight('Sir Lancelot', 10, lock)
second_knight = Knight("Sir Galahad", 20, lock)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
