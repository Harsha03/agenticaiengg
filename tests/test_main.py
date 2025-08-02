import unittest
from src import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # This just checks the main function runs without error
        main.main()

if __name__ == "__main__":
    unittest.main()
