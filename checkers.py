from cells import *
from board import print_board


def linear_check(line, possibilities):
    for num in line:
        if num != 0 and num in possibilities:
            possibilities.remove(num)


def quadrant_check(board, i, j, possibilities):
    x = find_quadrant(i)
    y = find_quadrant(j)
    for row in range(x, x + 3):
        for col in range(y, y + 3):
            cell = board[row][col]
            if cell != 0 and cell in possibilities:
                possibilities.remove(cell)


def find_quadrant(x):
    if x > 5:
        return 6
    elif x > 2:
        return 3
    else:
        return 0


def all_found(board):
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number == 0:
                return False
    return True


def solve(board):
    cells = make_possibility_cells(board)
    counter = 0
    while not all_found(board):
        counter += 1
        for i, row in enumerate(board):
            for j, number in enumerate(row):
                key = make_key(i, j)
                if number == 0:
                    horizontal = row
                    linear_check(horizontal, cells[key])

                    vertical = [board[r][j] for r in range(9)]
                    linear_check(vertical, cells[key])

                    quadrant_check(board, i, j, cells[key])

                    if len(cells[key]) == 1:
                        board[i][j] = cells[key].pop()
        print('After the {} cycle'.format(counter))
        print_board(board)
    print('Solved in {} cycles'.format(counter))
    return board
