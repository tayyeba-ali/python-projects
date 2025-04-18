import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()  # keep track of dug locations

    def make_new_board(self):
        # Construct a new board with bombs randomly planted
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue  

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue  # skip the original location
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col)) 

        if self.board[row][col] == '*':
            return False  # game over
        elif self.board[row][col] > 0:
            return True  # dig finished

        # dig recursively if it's a 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        # Returns a string representation of the board
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Create a string from visible_board
        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=lambda x: len(str(x)))
                )
            )

        indices_row = '   '
        cells = []
        for idx in range(self.dim_size):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % idx)
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(self.dim_size):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        return indices_row + string_rep

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)

    safe = True
    while len(board.dug) < (dim_size ** 2 - num_bombs):
        print(board)
        user_input = input("Where would you like to dig? (row,col): ")
        try:
            row, col = map(int, re.split(r',\s*', user_input.strip()))
        except ValueError:
            print("Invalid input. Please enter in the format: row,col")
            continue

        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("🎉 Congratulations, you won!")
    else:
        print("💥 Game Over! You hit a bomb.")
        # Reveal the board
        board.dug = [(r, c) for r in range(dim_size) for c in range(dim_size)]
        print(board)

if __name__ == '__main__':
    play()