from Movement import Movement
from constants import BLACK_SIDE, get_all_pieces, get_empty_screen
import os

def print_screen(screen):
    for base in screen:
        print(''.join(map(str, base)))
    return screen

def start_game(piece_code:str = 'j'):
    piece = get_all_pieces()[piece_code]
    screen_base = get_empty_screen()
    for i, values in enumerate(piece):
        for j, value in enumerate(values):
            screen_base[i][j] = value
    print_screen(screen_base)
    return screen_base

def print_piece(piece):
    for base in piece:
        print(''.join(map(str, base)))

def move_piece(movement:Movement, screen:list[list[str]]):
    new_screen = get_empty_screen()

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == BLACK_SIDE:
                new_row_index = 0
                new_column_index = 0
                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEAF:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        pass
                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    return (screen)
                else:
                    new_screen[new_row_index][new_column_index] = item
    os.system('clear')
    print_screen(new_screen)
    return new_screen

start_screen = start_game()
current_screen = move_piece(Movement.RIGHT, start_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)
current_screen = move_piece(Movement.RIGHT, current_screen)

current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
current_screen = move_piece(Movement.DOWN, current_screen)
