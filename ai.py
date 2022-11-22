
def did_win(board, ch):
    if board[0][0] == board[1][0] == board[2][0] == ch or \
            board[0][1] == board[1][1] == board[2][1] == ch or \
            board[0][2] == board[1][2] == board[2][2] == ch:
        return True
    if board[0][0] == board[0][1] == board[0][2] == ch or \
            board[1][0] == board[1][1] == board[1][2] == ch or \
            board[2][0] == board[2][1] == board[2][2] == ch:
        return True
    if board[0][0] == board[1][1] == board[2][2] == ch or board[0][2] == board[1][1] == board[2][0] == ch:
        return True


def is_draw(board):
    if not did_win(board, 'X') and not did_win(board, 'O'):
        for xpos in range(3):
            for ypos in range(3):
                if board[xpos][ypos] == '':
                    return False
        return True
    return False


def can_win(board, ch):
    for pos in range(9):
        if board[pos // 3][pos - 3 * (pos // 3)] == '':
            board[pos // 3][pos - 3 * (pos // 3)] = ch
            if did_win(board, ch):
                board[pos // 3][pos - 3 * (pos // 3)] = ''
                return pos
            else:
                board[pos // 3][pos - 3 * (pos // 3)] = ''


def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True


def get_dicts():
    plays_dict_for_x = {}
    plays_dict_for_o = {}
    first_o = [-1]

    def get_plays_x(tictactoe_board):
        max_best_pos = -2
        min_best_pos = 2
        best_pos = 0
        if is_draw(tictactoe_board):
            return 0
        if did_win(tictactoe_board, 'X'):
            return 1
        for o in range(9):
            if tictactoe_board[o // 3][o - 3 * (o // 3)] == '':
                if first_o[-1] > 0:
                    tictactoe_board[o // 3][o - 3 * (o // 3)] = 'O'
                else:
                    first_o.append(1)
            else:
                continue
            if did_win(tictactoe_board, 'O'):
                tictactoe_board[o // 3][o - 3 * (o // 3)] = ''
                return -1
            if is_draw(tictactoe_board):
                min_best_pos = min(min_best_pos, 0)
            for x in range(9):
                if tictactoe_board[x // 3][x - 3 * (x // 3)] == '':
                    tictactoe_board[x // 3][x - 3 * (x // 3)] = 'X'
                else:
                    continue
                n = get_plays_x(tictactoe_board)
                if max_best_pos <= n:
                    max_best_pos = n
                    best_pos = x
                tictactoe_board[x // 3][x - 3 * (x // 3)] = ''
            if not is_full(tictactoe_board):
                plays_dict_for_x[str(tictactoe_board)] = best_pos
            tictactoe_board[o // 3][o - 3 * (o // 3)] = ''
            min_best_pos = min(min_best_pos, max_best_pos)
            max_best_pos = -2
        return min_best_pos

    def get_plays_o(tictactoe_board):
        max_best_pos = -2
        min_best_pos = 2
        best_pos = 0
        if did_win(tictactoe_board, 'O'):
            return 1
        if is_draw(tictactoe_board):
            return 0
        for x in range(9):
            if tictactoe_board[x // 3][x - 3 * (x // 3)] == '':
                tictactoe_board[x // 3][x - 3 * (x // 3)] = 'X'
            else:
                continue
            if did_win(tictactoe_board, 'X'):
                tictactoe_board[x // 3][x - 3 * (x // 3)] = ''
                return -1
            if is_draw(tictactoe_board):
                min_best_pos = min(min_best_pos, 0)
                tictactoe_board[x // 3][x - 3 * (x // 3)] = ''
                continue
            for o in range(9):
                if tictactoe_board[o // 3][o - 3 * (o // 3)] == '':
                    tictactoe_board[o // 3][o - 3 * (o // 3)] = 'O'
                else:
                    continue
                n = get_plays_o(tictactoe_board)
                if max_best_pos <= n:
                    max_best_pos = n
                    best_pos = o
                tictactoe_board[o // 3][o - 3 * (o // 3)] = ''
            if not is_full(tictactoe_board):
                plays_dict_for_o[str(tictactoe_board)] = best_pos
            tictactoe_board[x // 3][x - 3 * (x // 3)] = ''
            min_best_pos = min(min_best_pos, max_best_pos)
            max_best_pos = -2
        return min_best_pos

    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    get_plays_o(board)
    get_plays_x(board)
    return plays_dict_for_o, plays_dict_for_x


