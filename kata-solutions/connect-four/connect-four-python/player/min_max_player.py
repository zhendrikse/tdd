from board.board import Disc
from board.array_board import ArrayBoard
from random import randint
from player.computer_player import ComputerPlayer

class MinMaxPlayer(ComputerPlayer):
  def __init__(self, game_board = ArrayBoard(), level = 0):
    self.board = game_board
    self.moves_ahead = level

  def switch_player(self, player):
    return Disc.YELLOW if player == Disc.RED else Disc.RED

  def pick_move(self, ratings):
    possible_moves = [index + 1 for index in range(7) if ratings[index] == max(ratings)]
    picked_move = randint(0, len(possible_moves) - 1)
    return possible_moves[picked_move]
    
  def rate_move(self, move, player = Disc.YELLOW, depth = 0):
    rating = 0
    #print(f"Move {self.board.current_disc} to {move} (Depth = {depth})")
    if self.board.has_connect_four():
      rating = self.moves_ahead * 3 - depth * 2
      rating = rating if player == Disc.RED else -rating
      #print(f"CONNECT FOUR WITH RATING {rating}")
    elif depth != self.moves_ahead:
      self.board.insert_disc_at(move, player)
      player = self.switch_player(player)
      for move in range(1, self.board.get_col_count() + 1):
        rating += self.rate_move(move, player, depth + 1) if self.board.is_valid_move(move) else 0
      self.board.undo_last_move()

    #print(f"Returning rating = {rating}")
    return rating
    
  def calculate_next_move(self):
    ratings = [0] * self.board.get_col_count()
    for move in range(1, self.board.get_col_count() + 1):
      ratings[move -1] = self.rate_move(move) \
        if self.board.is_valid_move(move) else -1000
    
    print(str(ratings))
    return self.pick_move(ratings)
