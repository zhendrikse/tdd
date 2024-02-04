from mamba import description, it, _it, fit, context, before
from expects import expect, equal, raise_error, be_true, be_false, be

from board.board import Board, Disc
from board.array_board import ArrayBoard

with description(Board) as self:
    with context("Given an new board"):
        with before.each:
            self.board = ArrayBoard()

        with it("cannot accept negative columns"):
            expect(lambda: self.board.insert_disc_at(-1, Disc.RED)).to(raise_error(ValueError, "Illegal move"))

        with it("signals no connect four"):
            expect(self.board.has_connect_four()).to(equal(None))

        with it("cannot stack more than 6 plies"):
            for i in range(6):
                self.board.insert_disc_at(1, Disc.RED)
            expect(lambda: self.board.insert_disc_at(1, Disc.RED)).to(raise_error(ValueError, "Illegal move"))

        with description("After insertion of one disc"):
            with it("has one disc in that column"):
                self.board.insert_disc_at(1, Disc.RED)
                expect(self.board.amount_discs_in_col(0)).to(equal(1))
            with it("can undo moves"):
                self.board.insert_disc_at(1, Disc.RED)
                self.board.insert_disc_at(1, Disc.RED)
                self.board.undo_last_move()
                expect(self.board.amount_discs_in_col(0)).to(equal(1))
                self.board.undo_last_move()
                expect(self.board.amount_discs_in_col(0)).to(equal(0))

    with description("Given a red horizontal connect four"):
        with it("returns the winning color"):
            expect(ArrayBoard.from_string("4433562").has_connect_four()).to(be_true)

    with description("Given a red vertical connect four"):
        with it("returns the winning color"):
            expect(ArrayBoard.from_string("1212121").has_connect_four()).to(be_true)

    with description("Given a red diagonal connect four"):
        with it("returns the winning color"):
            board = ArrayBoard.from_string("123456712345671234567626")
            # print(str(board))
            expect(board.has_connect_four()).to(be_true)

    with description("Given a yellow horizontal connect four"):
        with it("returns the winning color"):
            expect(ArrayBoard.from_string("12345674433562").has_connect_four()).to(be_true)
            expect(ArrayBoard.from_string("35363341174415").has_connect_four()).to(be_true)

    with description("Given a yellow vertical connect four"):
        with it("returns the winning color"):
            expect(ArrayBoard.from_string("13234353").has_connect_four()).to(be_true)

    with description("Given a yellow diagonal connect four"):
        with it("returns the winning color"):
            board = ArrayBoard.from_string("123456712345671234567113")
            # print(str(board))
            expect(board.has_connect_four()).to(be_true)

    with description("Board with diagonal 4"):
        with it("does not signal a connect four"):
            board = ArrayBoard.from_string("354244323325526527437377745666171416")
            expect(board.has_connect_four()).to(be_true)

    with description("Given a board"):
        with _it("determines the bottom-up diagonals"):
            board = ArrayBoard.from_string("1234567123456712345671234")
            # print(str(board))
            expect(str(board.bottom_up_diagonal_as_string(0, 3))).to(equal("2220"))
            expect(str(board.bottom_up_diagonal_as_string(1, 3))).to(equal("11100"))
            expect(str(board.bottom_up_diagonal_as_string(2, 3))).to(equal("222000"))
            expect(str(board.bottom_up_diagonal_as_string(3, 3))).to(equal("111100"))
            expect(str(board.bottom_up_diagonal_as_string(4, 3))).to(equal("22200"))
            expect(str(board.bottom_up_diagonal_as_string(5, 3))).to(equal("1100"))

        with _it("determines the top-down diagonals"):
            board = ArrayBoard.from_string("1234567123456712345671234")
            # print(str(board))
            expect(str(board.top_down_diagonal_as_string(0, 3))).to(equal("2222"))
            expect(str(board.top_down_diagonal_as_string(1, 3))).to(equal("01111"))
            expect(str(board.top_down_diagonal_as_string(2, 3))).to(equal("002222"))
            expect(str(board.top_down_diagonal_as_string(3, 3))).to(equal("001111"))
            expect(str(board.top_down_diagonal_as_string(4, 3))).to(equal("00022"))
            expect(str(board.top_down_diagonal_as_string(5, 3))).to(equal("0001"))
