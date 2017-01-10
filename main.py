#! python3
from sys import argv
from board import *
from checkers import solve


def main(path):
    board = load_board(path)
    board = solve(board)
    print_board(board)

if __name__ == "__main__":
    main(argv[1])
