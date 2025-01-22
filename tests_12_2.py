import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def __str__(self):
        return self.name


class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        while len(results) < len(self.runners):
            for runner in self.runners:
                if runner.distance < self.distance:
                    runner.run()
                if runner.distance >= self.distance and runner not in results.values():
                    results[len(results) + 1] = runner
        return results


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner1))
        self.assertEqual(output[2], str(self.runner3))

    def test_race_andrew_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner2))
        self.assertEqual(output[2], str(self.runner3))

    def test_race_usain_andrew_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        output = {place: str(participant) for place, participant in results.items()}
        print(output)

        self.assertEqual(output[1], str(self.runner1))
        self.assertEqual(output[2], str(self.runner2))
        self.assertEqual(output[3], str(self.runner3))


if __name__ == '__main__':
    unittest.main()