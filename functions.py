def find_next_empty_position(puzzle):
    """Finds the nex empty (represented with -1) position ((row, col)) in the puzzle.
    Returns (row,col) or (None, None) if there is none"""

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None


def is_valid_guess(puzzle, guess, row, col):
    """Figures out if the guess at (row,col) is a valid one.
    Returns True or False"""

    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    """Solves sudoku using backtracking. The puzzle is list of lists where each inner list is a row of the 9X9 square
    Returns whether a solution exists and mutates the puzzle to be the solution (if one exists)"""

    # choose a position to start guessing
    row, col = find_next_empty_position(puzzle)

    if row is None:
        return True

    # if there is a place to put a number, the "guess" between 1 and 9
    for guess in range(1, 10):
        # check if the guess is valid
        if is_valid_guess(puzzle, guess, row, col):
            # if it is a valid guess, then place it at the spot on the puzzle
            puzzle[row][col] = guess
            # then recursively call the solver
            if solve_sudoku(puzzle):
                return True

        # if not valid or if nothing returns True, then  backtrack and try a new number
        puzzle[row][col] = -1

    # if none of the guesses work then the puzzle has no solution
    return False
