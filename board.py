def load_board(path):
    board = []
    with open(path) as file:
        for line in file:
            board.append([int(i) for i in line.split(',')])
    return board


def print_board(board):
    for i, row in enumerate(board):
        print(row)
