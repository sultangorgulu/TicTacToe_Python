import copy

# Oyun tahtasının temsili
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Oyuncu sembolleri
HUMAN = 'O'
COMPUTER = 'X'

# Kazanma kombinasyonlarI
WIN_COMBO = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')


def is_winner(board, player):
    for combo in WIN_COMBO:
        if all(board[row][col] == player for row, col in combo):
            return True
    return False


def is_board_full(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))


def evaluate(board):
    if is_winner(board, COMPUTER):
        return 1
    elif is_winner(board, HUMAN):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None


def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    if result is not None:
        return result

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = COMPUTER
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = HUMAN
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval


def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = COMPUTER
                eval = minimax(board, 0, False)
                board[row][col] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move


def main():
    while True:
        print_board(board)
        if not is_board_full(board):
            human_move = input("Lütfen oynayın (örnek: 1 2): ").split()
            if len(human_move) != 2:
                print("Hatalı oynadınız, tekrar oynayın.")
                continue
            row, col = map(int, human_move)
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = HUMAN
            else:
                print("Hatalı oynadınız, tekrar oynayın.")
                continue
        else:
            print("Oyun berabere.")
            break

        if is_winner(board, HUMAN):
            print_board(board)
            print("Kazandınız! Tebrikler!")
            break

        if is_board_full(board):
            print_board(board)
            print("Oyun berabere.")
            break

        comp_move = best_move(copy.deepcopy(board))
        board[comp_move[0]][comp_move[1]] = COMPUTER

        if is_winner(board, COMPUTER):
            print_board(board)
            print("Bilgisayar kazandı. Kaybettiniz.")
            break


if __name__ == "__main__":
    main()
