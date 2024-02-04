from typing import List
from collections import deque


class Player:
    def __init__(self, name: str):
        self.name = name
        self.purse = 0
        self.board_position = 0
        self.inPenaltyBox = False

    def add_coin(self) -> None:
        self.purse += 1
        print(repr(self) + " now has " + str(self.purse) + " Gold Coins.")

    def has_won(self) -> bool:
        return self.purse == 6

    def add_to_board_position(self, steps: int) -> None:
        self.board_position += steps
        if self.board_position > 11:
            self.board_position -= 12
        print(repr(self) + "'s new location is " + str(self.board_position))

    def __repr__(self):
        return self.name


class Questions:
    def __init__(self):
        # https://realpython.com/linked-lists-python/
        self.popQuestions = deque()
        self.scienceQuestions = deque()
        self.sportsQuestions = deque()
        self.rockQuestions = deque()
        for i in range(50):
            self.popQuestions.append("Pop Question " + str(i))
            self.scienceQuestions.append("Science Question " + str(i))
            self.sportsQuestions.append("Sports Question " + str(i))
            self.rockQuestions.append("Rock Question " + str(i))

    def current_category(self, index: int) -> str:
        rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science",
                             "Sports"]
        if index <= 10:
            return rank_category_map[index]
        else:
            return "Rock"

    def ask_question(self, index: int) -> None:
        if self.current_category(index) == "Pop":
            print(self.popQuestions.popleft())
        if self.current_category(index) == "Science":
            print(self.scienceQuestions.popleft())
        if self.current_category(index) == "Sports":
            print(self.sportsQuestions.popleft())
        if self.current_category(index) == "Rock":
            print(self.rockQuestions.popleft())


class Players:
    def __init__(self, player1: Player, player2: Player, others: [Player] = []):
        self.players: List[Player] = []
        self.add(player1)
        self.add(player2)
        for player in others:
            self.add(player)

        self.currentPlayer = 0
        self.current_player = self.players[self.currentPlayer]

    def add(self, player: Player) -> bool:
        self.players.append(player)
        print(repr(player) + " was added")
        print("They are player number " + str(len(self.players)))
        return True

    def next_player(self) -> None:
        self.currentPlayer += 1
        if self.currentPlayer == len(self.players):
            self.currentPlayer = 0
        self.current_player = self.players[self.currentPlayer]


class Game:
    def __init__(self, player1: Player, player2: Player, others: [Player] = []):
        self.participants: Players = Players(player1, player2, others)
        self.questions = Questions()
        self.isGettingOutOfPenaltyBox: bool = False

    def roll(self, roll: int) -> None:
        print(repr(self.participants.current_player) + " is the current player")
        print("They have rolled a " + str(roll))

        if self.participants.current_player.inPenaltyBox:
            if roll % 2 != 0:
                self.isGettingOutOfPenaltyBox = True
                print(
                    repr(self.participants.current_player) +
                    " is getting out of the penalty box")
                self.move_player_and_ask_question(roll)
            else:
                print(
                    repr(self.participants.current_player) +
                    " is not getting out of the penalty box")
                self.isGettingOutOfPenaltyBox = False
        else:
            self.move_player_and_ask_question(roll)

    def move_player_and_ask_question(self, roll: int) -> None:
        self.participants.current_player.add_to_board_position(roll)

        print("The category is " + self.questions.current_category(self.participants.current_player.board_position))
        self.questions.ask_question(self.participants.current_player.board_position)

    def was_correctly_answered(self) -> bool:
        if self.participants.current_player.inPenaltyBox:
            if self.isGettingOutOfPenaltyBox:
                print("Answer was correct!!!!")

                self.participants.next_player()
                self.participants.current_player.add_coin()

                winner = self.did_player_win()

                return winner
            else:
                self.participants.next_player()
                return True
        else:
            print("Answer was corrent!!!!")
            self.participants.current_player.add_coin()

            winner = self.did_player_win()
            self.participants.next_player()

            return winner

    def wrong_answer(self) -> bool:
        print("Question was incorrectly answered")
        print(
            repr(self.participants.current_player) +
            " was sent to the penalty box")
        self.participants.current_player.inPenaltyBox = True

        self.participants.next_player()
        return True

    def did_player_win(self) -> bool:
        return not self.participants.current_player.has_won()
