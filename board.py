def load_board(path):
    result = []
    with open(path) as file:
        for line in file:
            result.append([int(i) for i in line.split(',')])
    return result


def print_board(board):
    for i, row in enumerate(board):
        print(row)
