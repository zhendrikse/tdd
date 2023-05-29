import unittest
from approvaltests.approvals import verify
from subprocess import run

class GameTest(unittest.TestCase):
    def test_trivia_game(self):
        output = run(["python", "game_runner.py"], capture_output=True).stdout
        verify(output.decode())

if __name__ == "__main__":
    unittest.main()

