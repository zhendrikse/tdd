from board.board import Disc
from board.array_board import ArrayBoard
from player.connect_4_rating_player import ConnectFourRatingPlayer

class Game:
  def __init__(self, game_board = ArrayBoard(), level = 0):
    self.board = game_board
    self.computer = ConnectFourRatingPlayer(game_board, level)

  def play(self):
    # TODO Do zo lang als het bord nog niet vol is, anders remise
    while True:
      print(str(self.board))
  
      # Human
      val = input("Enter your row: ")
      self.board.insert_disc_at(int(val), Disc.RED)
      if self.board.has_connect_four():
        return Disc.RED
  
      # Commputer
      move = self.computer.calculate_next_move()
      print(f"Computer plays {move}")
      self.board.insert_disc_at(move, Disc.YELLOW)
      if self.board.has_connect_four():
        return Disc.YELLOW
    
def main():
  game = Game(level = 4)
  winner = game.play()
  print(str(game.board))
  print(str(Disc.RED if winner == Disc.RED else Disc.YELLOW) + " wins!")

if __name__ == "__main__":
    main()
