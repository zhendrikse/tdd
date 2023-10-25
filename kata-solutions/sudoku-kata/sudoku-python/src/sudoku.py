import itertools
from dataclasses import dataclass


@dataclass(frozen=True)
class SudokuIndex(object):
    row: int
    column: int

    def next_row(self) -> int:
        return (self.row * 9 + self.column + 1) // 9

    def next_column(self) -> int:
        return (self.row * 9 + self.column + 1) % 9

    def next(self):
        return SudokuIndex(self.next_row(), self.next_column())

    def is_last_cell(self) -> bool:
        return self.row == 9 and self.column == 0


class Sudoku:
    def __init__(self, puzzle_string: str) -> None:
        puzzle_string = puzzle_string.replace('.', '0')

        self.puzzle = [[0] * 9 for _ in range(9)]
        for i in range(81):
            self.puzzle[i // 9][i % 9] = int(puzzle_string[i])

    def duplicate_cell_value_in_row(self, index: SudokuIndex) -> bool:
        return self.puzzle[index.row].count(self.cell_value_at(index)) > 1

    def duplicate_cell_value_in_column(self, index: SudokuIndex) -> bool:
        transposed_puzzle = [list(i) for i in zip(*self.puzzle)]
        return transposed_puzzle[index.column].count(self.cell_value_at(index)) > 1

    def duplicate_cell_value_in_3_3_block(self, index: SudokuIndex) -> bool:
        row = index.row
        column = index.column
        return any((i != row or j != column)
                   and self.puzzle[row][column] == self.puzzle[i][j]
                   for i, j in itertools.product(
            range((row // 3) * 3, (row // 3) * 3 + 3),
            range((column // 3) * 3, (column // 3) * 3 + 3),
        ))

    def cell_value_at(self, index: SudokuIndex) -> int:
        return self.puzzle[index.row][index.column]

    def cell_value_allowed(self, index: SudokuIndex) -> bool:
        if self.duplicate_cell_value_in_row(index):
            return False
        if self.duplicate_cell_value_in_column(index):
            return False
        return not self.duplicate_cell_value_in_3_3_block(index)

    def is_cell_empty(self, index: SudokuIndex) -> bool:
        return self.cell_value_at(index) == 0

    def solve(self, index: SudokuIndex) -> bool:
        # arrived at last cell? --> done, so return
        if index.is_last_cell():
            return True

        # go to next cell if cell value is given
        if not self.is_cell_empty(index):
            return self.solve(index.next())

            # build tree for each allowed value 1...9
        for i in range(1, 10):
            self.puzzle[index.row][index.column] = i
            if not self.cell_value_allowed(index):
                continue
            if self.solve(index.next()):
                return True

        # backtrack because at this point all values failed
        self.puzzle[index.row][index.column] = 0
        return False
