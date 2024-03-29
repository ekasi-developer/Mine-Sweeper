import random


MIN_NUMBER_COLUMNS = 4
MIN_NUMBER_ROWS = 4


def generate(column: int, row: int, empty=False) -> list:
    board = []
    for row_index in range(row):
        board.append([])
        for column_index in range(0, column):
            board[row_index].append(" " if empty else random.randint(0, 2))
    return board


def header(board: list) -> str:
    header_string = ""
    for i, row in enumerate(board[0]):
        header_string += f"{' ' * 5}{i}" if i == 0 else f"{' ' * 3}{i}"
    return f"{header_string}\n {'-' * (len(header_string)+1)}\n"


def display(board: list) -> str:
    board_string = header(board)
    for row_index, row in enumerate(board):
        for column_index, column in enumerate(row):
            board_string += f" {row_index} | {column} |" if column_index == 0 else f" {column} |"
        board_string += "\n"
    return board_string


def row_exists(board: list, row: int) -> bool:
    return 0 <= row < len(board)


def column_exists(board: list, column: int) -> bool:
    return 0 <= column < len(board[0])


def make_move(board: list, row: int, column: int) -> int:
    return board[row][column]


def is_bomb(box: int) -> bool:
    return box == 0
