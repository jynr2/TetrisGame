from enum import Enum

WHITE_SIDE = '🔲'
BLACK_SIDE = '🔳'

__PIECE_I = [
    [BLACK_SIDE, BLACK_SIDE, BLACK_SIDE, BLACK_SIDE]
]

__PIECE_J = [
    [BLACK_SIDE, WHITE_SIDE, WHITE_SIDE],
    [BLACK_SIDE, BLACK_SIDE, BLACK_SIDE]
]

__PIECE_L = [
    [WHITE_SIDE, WHITE_SIDE, BLACK_SIDE],
    [BLACK_SIDE, BLACK_SIDE, BLACK_SIDE]
]

__PIECE_O = [
    [BLACK_SIDE, BLACK_SIDE],
    [BLACK_SIDE, BLACK_SIDE]
]

__PIECE_S = [
    [WHITE_SIDE, BLACK_SIDE, BLACK_SIDE],
    [BLACK_SIDE, BLACK_SIDE, WHITE_SIDE]
]

__PIECE_T = [
    [WHITE_SIDE, BLACK_SIDE, WHITE_SIDE],
    [BLACK_SIDE, BLACK_SIDE, BLACK_SIDE]
]

__PIECE_Z = [
    [BLACK_SIDE, BLACK_SIDE, WHITE_SIDE],
    [WHITE_SIDE, BLACK_SIDE, BLACK_SIDE]
]

def get_all_pieces() -> dict[str, list[list[str]]]:
    return {'i': __PIECE_I, 'j': __PIECE_J, 'l': __PIECE_L, 'o': __PIECE_O, 's': __PIECE_S, 't': __PIECE_T, 'z': __PIECE_Z}

def get_empty_screen()-> list[list[str]]:
    return [[WHITE_SIDE for _ in range(10)] for _ in range(10)]
