# Tic-Tac-Toe Game
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")


def check_winner(board, player):

    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True


    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def check_draw(board):
    return all([cell != " " for row in board for cell in row])


def play_game():

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]


        move = int(input(f"Player {current_player}, enter a number (1-9): ")) - 1
        row, col = divmod(move, 3)


        if 0 <= move < 9 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue


        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break


        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        turn += 1

play_game()
