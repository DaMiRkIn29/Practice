import unittest


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner1))
        self.assertEqual(output[2], str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_andrew_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner2))
        self.assertEqual(output[2], str(self.runner3))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_usain_andrew_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner1))
        self.assertEqual(output[2], str(self.runner2))
        self.assertEqual(output[3], str(self.runner3))


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Вася")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Миша")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Али")
        runner2 = Runner("Тайсон")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()