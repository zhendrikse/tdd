import io
from contextlib import redirect_stdout
from approvaltests.approvals import verify
from game_runner import GameRunner


class TestGame:
  def catch_output(self, func):
    result = io.StringIO()
    with redirect_stdout(result):
        func()
    return result.getvalue()

  def test_trivia_game(self):
    output = self.catch_output(GameRunner.main)
    verify(output)
