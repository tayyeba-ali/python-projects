from pprint import pprint

def find_empty(puzzle):
    for r in range(9):
        for c in range(9): #range(9) is 0 ,1 ,`2,3,4,5,6,7,8`
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no space in the puzzle are empty(-1)
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row] #get the row values of the puzzle
    if guess in row_vals: #if the guess is in the row values of the puzzle
        return False #return false
    
    #now the column
    col_vals = []
    for i in range (9):
        col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)] #get the column values of the puzzle
    if guess in col_vals:
        return False
    row_start = (row // 3)*3
    col_start = (col // 3)*3 #get the starting row and column of the puzzle

    for r in range(row_start, row_start + 3): #get the values of the 3x3 grid of the puzzle
        for c in range(col_start, col_start + 3): #get the values of the 3x3 grid of the puzzle
            if puzzle[r][c] == guess: #if the guess is in the 3x3 grid of the puzzle
                return False #return false
    return True

def solve_sudoku(puzzle):
    #step1 : choose somewhere in the puzzle to make a guess
    row, col = find_empty(puzzle) #find the empty space in the puzzle

    #ste 1.1: if there's nowhere left, then we're done because we have allowed valid inputs
    if row is None: #if there is no empty space in the puzzle
        return True #return true
    
    #step 2: if there is a space, then we need to guess a number between 1-9
    for guess in range(1, 10): #guess a number between 1-9
    #step 3 : 
        if is_valid(puzzle, guess, row, col):
         #step 3.1 : if this is valid , then place that guess on the puzzle
         puzzle[row][col] = guess #place the guess on the puzzle
         #now recuse using this puzzle
         #step 4:Recusrively call our solve_sudoku function
         if solve_sudoku(puzzle):
                return True
    #step 5 : if not valid OR if our guess does not solve then we need to reset the guess and try again
    #backtrack and try a new number
    puzzle[row][col] = -1 #reset the guess to 0
#step 6: if none of the numbers work, then this puzzle is unsolvable
    return False #return false


if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))

    pprint(example_board)