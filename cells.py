def make_key(i, j):
    return str(i) + str(j)


def make_possibility_cells(board):
    cells = {}
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            key = make_key(i, j)
            if number != 0:
                cells[key] = number
            else:
                cells[key] = [i for i in range(1, 10)]
    return cells
