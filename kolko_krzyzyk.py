from collections import OrderedDict

import k_k_validator


def create_board():
    list_of_1 = [1, 2, 3]
    list_of_2 = [4, 5, 6]
    list_of_3 = [7, 8, 9]
    return [list_of_1, list_of_2, list_of_3]


def input_num():
    while True:
        try:
            print("Podaj liczbę: ")
            return int(input())
        except ValueError:
            print("To nie jest liczba! Spróbuj jeszcze raz")


def board_controller(number, board, marker):
    for i in board:
        for z in range(len(i)):
            if i[z] == number:
                i[z] = marker
    return board


def show_board(a, b, c):
    print(" {}|{}|{} \n {}|{}|{} \n {}|{}|{} ".format(*a, *b, *c))


def game():
    board = create_board()
    game_goes_on = True
    while game_goes_on:
        a, b, c = board_controller(input_num(), board, 'o')
        show_board(a, b, c)
        if k_k_validator.validator_kolko_krzyzyk(board) == 0:
            print("Wygraly o")
            game_goes_on = False
        else:
            a, b, c = board_controller(input_num(), board, 'x')
            show_board(a, b, c)
            if k_k_validator.validator_kolko_krzyzyk(board) == 1:
                print("Wygraly x")
                game_goes_on = False
            else:
                print("Remis")
                game_goes_on = False


def make_round(board):
    x_won = check(board, 1)
    o_won = check(board, 2)
    was_draw = check(board, 3)
    if x_won or o_won or was_draw:
        show_score(o_won, x_won)
        return False
    return True


def show_score(o_won, x_won):
    if x_won:
        print("Wygrały x")
    elif o_won:
        print("Wygrały o")
    else:
        print("Remis")


def check(board, status):
    if k_k_validator.validator_kolko_krzyzyk(board) == status:
        return True
    return False


def move(board, marker):
    board_controller(input_num(), board, marker)


def game_2():
    board = create_board()
    while True:
        move(board, 'x')
        show_board(*board)
        if not make_round(board):
            break
        move(board, 'o')
        show_board(*board)
        if not make_round(board):
            break


game_2()
