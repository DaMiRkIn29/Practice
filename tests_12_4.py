import unittest
import logging
from runner import Runner

logging.basicConfig(
    level=logging.INFO, filename='runner_tests.log', filemode='w',
    encoding='utf-8', format='%(levelname)s: %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Вося', -10)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning("Неверная скорость для Runner: %s", ve)

    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning("Неверный тип данных для объекта Runner: %s", te)


if __name__ == "__main__":
    unittest.main()
