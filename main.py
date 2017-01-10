board = [[1, 6, 5, 7, 9, 4, 0, 3, 8],
         [4, 0, 7, 0, 0, 2, 0, 5, 0],
         [9, 3, 0, 0, 0, 6, 0, 0, 4],

         [8, 1, 0, 4, 0, 5, 0, 0, 2],
         [5, 7, 6, 2, 3, 9, 4, 0, 0],
         [2, 0, 0, 6, 0, 1, 0, 7, 5],

         [3, 0, 1, 5, 0, 7, 8, 4, 9],
         [6, 9, 0, 0, 0, 0, 5, 2, 7],
         [0, 5, 0, 0, 2, 8, 1, 0, 3]]


def make_key(i, j):
    return str(i) + str(j)


def linear_check(line, possibilities):
    for num in line:
        if num != 0 and num in possibilities:
            possibilities.remove(num)


def quadrant_check(i, j, possibilities):
    x = choose(i)
    y = choose(j)
    for row in range(x, x + 3):
        for column in range(y, y + 3):
            if board[row][column] != 0 and board[row][column] in possibilities:
                possibilities.remove(board[row][column])


def choose(x):
    if x > 5: return 6
    elif x > 2: return 3
    return 0


cells = {}
for i, row in enumerate(board):
    for j, number in enumerate(row):
        cells[make_key(i, j)] = [i for i in range(1, 10)]

for times in range(100):
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            key = make_key(i, j)
            if number != 0:
                cells[key] = number
            else:
                linear_check(row, cells[key])
                linear_check([board[r][j] for r in range(0, 9)], cells[key])
                quadrant_check(i, j, cells[key])

                if len(cells[key]) == 1:
                    board[i][j] = cells[key].pop()


for i, row in enumerate(board):
    if i % 3 == 0: print()
    print(row)
