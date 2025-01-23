import unittest
from tests_12_3 import TournamentTest, RunnerTest


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
