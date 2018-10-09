half_game = [['x', 2, 3],
             [4, 5, 6],
             [7, 'o', 9]]
won_game_x = [['x', 'x', 'x'],
              ['o', 5, 'o'],
              [7, 'o', 9]]
won_game_o = [['x', 'x', 'o'],
              [4, 'o', 6],
              ['o', 'x', 9]]
no_winner = [['x', 'o', 'o'],
             ['o', 'x', 'x'],
             ['x', 'o', 'o']]


def validator_kolko_krzyzyk(board):
    if is_half_game(board) == 9:
        if is_won(board, 'x'):
            return 1
        elif is_won(board, 'o'):
            return 2
        else:
            return 3
    return False


def is_half_game(board):
    licz = 0
    for i in board:
        for z in i:
            if (z == 'x') or (z == 'o'):
                licz += 1
    return licz


def is_won(board, marker):
    if check_horizontal(board, marker) or check_vertical(board, marker) or check_cross(board, marker):
        return True
    return False


def check_horizontal(board, marker):
    for i in board:
        if i == [marker, marker, marker]:
            return True
    return False


def check_vertical(board, marker):
    for i in range(len(board[0])):
        list_value = []
        for z in board:
            list_value.append(z[i])
        if list_value == [marker, marker, marker]:
            return True
    return False


def check_cross(board, marker):
    if ([board[0][0], board[1][1], board[2][2]] == [marker, marker, marker]) or (
            [board[0][2], board[1][1], board[2][0]] == [marker, marker, marker]):
        return True
    return False


won = [["x", 2, "o"], [4, 5, 6], [7, 8, 9]]

aaa = validator_kolko_krzyzyk(won)
print(aaa)
