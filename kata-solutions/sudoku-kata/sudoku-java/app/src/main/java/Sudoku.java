public class Sudoku {
  /** The puzzle to solve. */
  private int[][] puzzle = new int[9][9];
  private SudokuValidator validator;

  public static class SudokuIndex {
    public final int row;
    public final int column;

    public SudokuIndex(final int row, final int column) {
      this.row = row;
      this.column = column;
    }

    private int nextRow() {
      return nextColumn() == 0 ? this.row + 1 : this.row;
    }

    private int nextColumn() {
      return this.column + 1 > 8 ? 0 : this.column + 1;
    }

    public SudokuIndex next() {
      return new SudokuIndex(nextRow(), nextColumn());
    }
  }

  public Sudoku(int[][] puzzle) {
    this.puzzle = puzzle;
    this.validator = new SudokuValidator(puzzle);
  }

  public static Sudoku fromString(String sudokuString) {
    int[][] puzzle = new int[9][9];
    var strs = sudokuString.strip().replace('.', '0').toCharArray();
    for (int i = 0; i < 81; i++) {
      puzzle[i / 9][i % 9] = strs[i] - '0';
    }
    return new Sudoku(puzzle);
  }

  private boolean isCellEmpty(final SudokuIndex index) {
    return puzzle[index.row][index.column] == 0;
  }

  private boolean isLastCell(final SudokuIndex index) {
    return index.row == 9 && index.column == 0;
  }

  public boolean solve(final SudokuIndex index) {
    // arrived at last cell? --> done, so return
    if (isLastCell(index))
      return true; 

    // go to next cell if cell is not emtpy
    if (!isCellEmpty(index))
      return solve(index.next()); 

    // try new value for empty cell
    for (int i = 1; i < 10; i++) {
      puzzle[index.row][index.column] = i;
      if(!validator.isValid(index)) continue;
      if (solve(index.next())) return true;
    }
    
    puzzle[index.row][index.column] = 0;
    return false;
  }

  public String toString() {
    return print(puzzle);
  }

  /**
   * Print a square matrix.
   *
   * @param matrix Matrix to print.
   * @return Output of matrix as String.
   */
  private String print(int[][] matrix) {
    final StringBuffer out = new StringBuffer();
    out.append("+-----------------+\n");
    for (int row = 0; row < 9; row++) {
      out.append("|");
      for (int column = 0; column < 9; column++) {
        out.append(matrix[row][column]).append("|");
      }
      out.append("\n");
    }
    out.append("+-----------------+");
    return out.toString();
  }
}
