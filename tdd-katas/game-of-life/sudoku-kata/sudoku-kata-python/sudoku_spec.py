from mamba import description, it, fit, context, before
from expects import expect, equal, raise_error, be_true, be_false
from sudoku import Sudoku, SudokuIndex

with description(SudokuIndex) as self:
  with context("Determining next row and column"):
    with it("advances by default only the column by one"):
      expect(SudokuIndex(0, 0).next_column()).to(equal(1))
    with it("stays in the same row by default"):
      expect(SudokuIndex(0, 0).next_row()).to(equal(0))
    with it("advances the last column to the next row"):
      expect(SudokuIndex(0, 8).next_column()).to(equal(0))
    with it("advances to the next row when on last column"):
      expect(SudokuIndex(0, 8).next_row()).to(equal(1))
    with it("identifies the last cell has been covered"):
      expect(SudokuIndex(9, 0).is_last_cell()).to(be_true)    
    with it("identifies the last cell has not been reached yet"):
      expect(SudokuIndex(8, 7).is_last_cell()).to(be_false)    

with description(Sudoku) as self:
  with context("Given a string"):
    with before.each:
      puzzle_string = ".5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4"
      self.sudoku = Sudoku(puzzle_string)

    with it("initializes the puzzle"):
      expect(self.sudoku.puzzle[0][0]).to(equal(0))
      expect(self.sudoku.puzzle[8][8]).to(equal(4))

    with it("identifies a given cell value is present in a row"):
      self.sudoku.puzzle[0][0] = 3
      expect(self.sudoku.duplicate_cell_value_in_row(SudokuIndex(0, 0))).to(be_true)

    with it("identifies a given cell value is absent in a row"):
      self.sudoku.puzzle[0][0] = 2
      expect(self.sudoku.duplicate_cell_value_in_row(SudokuIndex(0, 0))).to(be_false)

    with it("identifies a given cell value is present in a column"):
      self.sudoku.puzzle[0][0] = 3
      expect(self.sudoku.duplicate_cell_value_in_column(SudokuIndex(0, 0))).to(be_true)

    with it("identifies a given cell value is absent in a column"):
      self.sudoku.puzzle[0][0] = 2
      expect(self.sudoku.duplicate_cell_value_in_column(SudokuIndex(0, 0))).to(be_false)

    with it("identifies a given cell value is present in a 3x3 block"):
      self.sudoku.puzzle[0][0] = 3
      expect(self.sudoku.duplicate_cell_value_in_3_3_block(SudokuIndex(0, 0))).to(be_true)

    with it("identifies a given cell value is absent in a 3x3 block"):
      self.sudoku.puzzle[0][0] = 2
      expect(self.sudoku.duplicate_cell_value_in_3_3_block(SudokuIndex(0, 0))).to(be_false)

    with it("combines all three rules to find a valid value"):
      self.sudoku.puzzle[0][0] = 3
      expect(self.sudoku.cell_value_allowed(SudokuIndex(0, 0))).to(be_false)

    with it("combines all three rules to find a valid value"):
      self.sudoku.puzzle[0][0] = 2
      expect(self.sudoku.cell_value_allowed(SudokuIndex(0, 0))).to(be_true)

    with it("identifies an empty cell"):
      expect(self.sudoku.is_cell_empty(SudokuIndex(0, 0))).to(be_true)

    with it("identifies a given cell"):
      expect(self.sudoku.is_cell_empty(SudokuIndex(0, 1))).to(be_false)

    with it("solves the puzzle"):
      solution_string = "652483917978162435314975628825736149791824563436519872269348751547291386183657294"
      solved_puzzle = Sudoku(solution_string)
      expect(self.sudoku.solve(SudokuIndex(0, 0))).to(be_true)
      for i in range(81):
        expect(self.sudoku.puzzle[i // 9][i % 9]).to(equal(solved_puzzle.puzzle[i // 9][i % 9]))

