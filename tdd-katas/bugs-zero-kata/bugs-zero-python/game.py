from typing import List
from collections import deque

class Game:
    def __init__(self):
        self.players: List[str] = []
        self.places: List[int] = [0] * 6 
        self.purses: List[int] = [0] * 6
        self.inPenaltyBox: List[bool] = [False] * 6

        # https://realpython.com/linked-lists-python/
        self.popQuestions = deque()
        self.scienceQuestions = deque()
        self.sportsQuestions = deque()
        self.rockQuestions = deque()

        self.currentPlayer = 0
        self.isGettingOutOfPenaltyBox: bool = False

        for i in range(50):
            self.popQuestions.append("Pop Question " + str(i))
            self.scienceQuestions.append("Science Question " + str(i))
            self.sportsQuestions.append("Sports Question " + str(i))
            self.rockQuestions.append(self.createRockQuestion(i))

    def createRockQuestion(self, index: int) -> str:
        return "Rock Question " + str(index)

    def isPlayable(self) -> bool:
        return (self.howManyPlayers() >= 2)

    def add(self, playerName: str) -> bool:
        self.players.append(playerName)
        self.places[self.howManyPlayers()] = 0
        self.purses[self.howManyPlayers()] = 0
        self.inPenaltyBox[self.howManyPlayers()] = False
        print(playerName + " was added")
        print("They are player number " + str(len(self.players)))
        return True

    def howManyPlayers(self) -> int:
        return len(self.players)

    def roll(self, roll: int) -> None:
        print(self.players[self.currentPlayer] + " is the current player")
        print("They have rolled a " + str(roll))

        if self.inPenaltyBox[self.currentPlayer]:
            if roll % 2 != 0:
                self.isGettingOutOfPenaltyBox = True
                print(
                    self.players[self.currentPlayer] +
                    " is getting out of the penalty box")
                self.movePlayerAndAskQuestion(roll)
            else:
                print(
                    self.players[self.currentPlayer] +
                    " is not getting out of the penalty box")
                self.isGettingOutOfPenaltyBox = False
        else:
            self.movePlayerAndAskQuestion(roll)

    def movePlayerAndAskQuestion(self, roll: int) -> None:
        self.places[self.currentPlayer] = self.places[self.currentPlayer] + roll
        if self.places[self.currentPlayer] > 11:
            self.places[self.currentPlayer] = self.places[self.currentPlayer] - 12

        print(self.players[self.currentPlayer] + "'s new location is " +
            str(self.places[self.currentPlayer]))
        print("The category is " + self.currentCategory())
        self.askQuestion()

    def askQuestion(self) -> None:
        if self.currentCategory() == "Pop":
            print(self.popQuestions.popleft())
        if self.currentCategory() == "Science":
            print(self.scienceQuestions.popleft())
        if self.currentCategory() == "Sports":
            print(self.sportsQuestions.popleft())
        if self.currentCategory() == "Rock":
            print(self.rockQuestions.popleft())

    def currentCategory(self) -> str:
        if self.places[self.currentPlayer] == 0: return "Pop"
        if self.places[self.currentPlayer] == 4: return "Pop"
        if self.places[self.currentPlayer] == 8: return "Pop"
        if self.places[self.currentPlayer] == 1: return "Science"
        if self.places[self.currentPlayer] == 5: return "Science"
        if self.places[self.currentPlayer] == 9: return "Science"
        if self.places[self.currentPlayer] == 2: return "Sports"
        if self.places[self.currentPlayer] == 6: return "Sports"
        if self.places[self.currentPlayer] == 10: return "Sports"
        return "Rock"

    def was_correctly_answered(self) -> bool:
        if self.inPenaltyBox[self.currentPlayer]:
            if self.isGettingOutOfPenaltyBox:
                print("Answer was correct!!!!")
                self.currentPlayer += 1
                if self.currentPlayer == len(self.players):
                    self.currentPlayer = 0
                self.purses[self.currentPlayer] += 1
                print(
                    self.players[self.currentPlayer] + " now has " +
                    str(self.purses[self.currentPlayer]) + " Gold Coins.")

                winner = self.didPlayerWin()

                return winner
            else:
                self.currentPlayer += 1
                if self.currentPlayer == len(self.players):
                    self.currentPlayer = 0
                return True
        else:
            print("Answer was corrent!!!!")
            self.purses[self.currentPlayer] += 1
            print(
                self.players[self.currentPlayer] + " now has " +
                str(self.purses[self.currentPlayer]) + " Gold Coins.")

            winner = self.didPlayerWin()
            self.currentPlayer += 1
            if self.currentPlayer == len(self.players):
                self.currentPlayer = 0

            return winner

    def wrong_answer(self) -> bool:
        print("Question was incorrectly answered")
        print(
            self.players[self.currentPlayer] +
            " was sent to the penalty box")
        self.inPenaltyBox[self.currentPlayer] = True

        self.currentPlayer += 1
        if self.currentPlayer == len(self.players):
            self.currentPlayer = 0
        return True

    def didPlayerWin(self) -> bool:
        return not self.purses[self.currentPlayer] == 6
