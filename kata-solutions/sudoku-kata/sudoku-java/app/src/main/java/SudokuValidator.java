class SudokuValidator
{
  private int[][] puzzle;

  public SudokuValidator(int[][] puzzle)
  {
    this.puzzle = puzzle;
  }

  private boolean isContentOfSquareAlreadyPresentInRow(int row, int column) {
      for (int checkColumn = 0; checkColumn < 9; checkColumn++) {
        if (checkColumn != column &&
           puzzle[row][column] == puzzle[row][checkColumn]) return true;
      }
      return false;   
    }

    private boolean isContentOfSquareAlreadyPresentInColumn(int row, int column) {
        for (int checkRow = 0; checkRow < 9; checkRow++) {
            if (checkRow != row &&
                puzzle[row][column] == puzzle[checkRow][column]) return true;
        }
        return false;   
    }

    private boolean isContentOfSquareAlreadyPresentInMiniSquare(int row, int column) {
        int blockRow = (row / 3) * 3;
        int blockColumn = (column / 3) * 3;
        for (int i = blockRow; i < (blockRow + 3); i++) {
            for (int j = blockColumn; j < (blockColumn + 3); j++) {
                if (i != row && j != column) {
                    if (puzzle[row][column] == puzzle[i][j]) return true;
                }
            }
        }
        return false;   
    }

    boolean isValid(final Sudoku.SudokuIndex index) {

        if (isContentOfSquareAlreadyPresentInRow(index.row, index.column)) {
          return false;
        }

        if (isContentOfSquareAlreadyPresentInColumn(index.row, index.column)) {
          return false;
        }

        if (isContentOfSquareAlreadyPresentInMiniSquare(index.row, index.column)) {
          return false;
        }

        return true;
    }
}