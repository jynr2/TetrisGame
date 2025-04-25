from Movement import Movement
from constants import BLACK_SIDE, WHITE_SIDE, get_all_pieces, get_empty_screen
import os

def print_screen(screen):
    for base in screen:
        print(''.join(map(str, base)))
    return screen

def start_game(piece_code:str = 'j', screen_base:list[list[str]] = []):
    piece = get_all_pieces()[piece_code]
    if screen_base == []:
        screen_base = get_empty_screen()
    for i, values in enumerate(piece):
        for j, value in enumerate(values):
            screen_base[i][j] = value
    print_screen(screen_base)
    return screen_base

def print_piece(piece):
    for base in piece:
        print(''.join(map(str, base)))


def move_piece_right(matriz:list[list[str]]):
    print(type(matriz))
    for row in matriz:
        for i in range(len(row) - 2, -1, -1):
            if row[i] == BLACK_SIDE and row[i + 1] == WHITE_SIDE:
                row[i + 1] = BLACK_SIDE
                row[i] = WHITE_SIDE
    return matriz

def mover_asteriscos_derecha(matriz: list[list[str]]):
    for row in matriz:
        for i in range(len(row) - 2, -1, -1):
            if row[i] == BLACK_SIDE and row[i + 1] == WHITE_SIDE:
                row[i + 1] = BLACK_SIDE
                row[i] = WHITE_SIDE
    
    return matriz

def move_piece_left(matriz:list[list[str]]):
    for row in matriz:
        for i in range(1, len(row)):
            if row[i] == BLACK_SIDE and row[i - 1] == WHITE_SIDE:
                row[i - 1] = BLACK_SIDE
                row[i] = WHITE_SIDE
    return matriz


def move_piece_down(matriz:list[list[str]]):
    rows = len(matriz)
    columns = len(matriz[0])
    for i in range(rows - 2, -1, -1):
        for j in range(columns):
            if matriz[i][j] == BLACK_SIDE and matriz[i + 1][j] == WHITE_SIDE:
                matriz[i + 1][j] = BLACK_SIDE
                matriz[i][j] = WHITE_SIDE
    return matriz


def move_piece(movement:Movement, screen:list[list[str]]) -> list[list[str]]:
    match movement:
        case Movement.DOWN:
            screen = move_piece_down(screen)
        case Movement.RIGHT:
            screen = mover_asteriscos_derecha(screen)
        case Movement.LEAF:
            screen = move_piece_left(screen)
        case Movement.ROTATE:
            pass
    os.system('clear')
    print_screen(screen)
    return screen


start_screen = start_game()
current_screen = move_piece(Movement.RIGHT, start_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
