from mamba import description, it, fit, context, _it, fdescription
from expects import expect, equal, raise_error, be_true, be_false, be

from game import Game
from board.board import Board

# with description(Game) as self:
#   with description("Ratings with one highest rating"):
#     with it("picks the move with the highest rating"):
#       expect(Game().pick_move([0,0,-1,-2,1,0,0])).to(equal(5))

#   with fdescription("Given a board"):
#     with it("prevents leathal move"):
#       board = Board.from_string("3742443552331")
#       game = Game(board)
#       move_ratings = game.rate_moves(game.board.current_disc)
#       #print(str(board))
#       #print(str(move_ratings))
#       expect(game.pick_move(move_ratings)).to(equal(2))
      
#     with it("identifies horizontal threat"):
#       board = Board.from_string("32415")
#       game = Game(game_board = board)
#       move_ratings = game.rate_moves(board.current_disc)
#       #print(str(board))
#       #print(str(move_ratings))
#       expect(game.pick_move(move_ratings)).to(be(6))
      
#     with it("identifies vertical threat"):
#       board = Board.from_string("32313")
#       game = Game(game_board = board)
#       move_ratings = game.rate_moves(board.current_disc)
#       # print(str(board))
#       # print(str(move_ratings))
#       expect(game.pick_move(move_ratings)).to(be(3))

#     with it("prevents double attack"):
#       board = Board.from_string("314")
#       game = Game(game_board = board)
#       move_ratings = game.rate_moves(board.current_disc)
#       print(str(board))
#       print(str(move_ratings))
#       expect(game.pick_move(move_ratings)).to(be(2))
      