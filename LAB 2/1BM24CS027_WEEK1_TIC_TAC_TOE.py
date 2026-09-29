# Tic-Tac-Toe using simple rule-based AI

board = [" " for i in range(9)]


def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def computer_move():

    # Computer tries to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if winner("O"):
                return

            board[i] = " "

    # Computer blocks the player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    # Take center
    if board[4] == " ":
        board[4] = "O"
        return

    # Take any empty position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


print("TIC-TAC-TOE")
print("You = X")
print("Computer = O")

for turn in range(9):

    show_board()

    # Player's turn
    if turn % 2 == 0:

        while True:
            try:
                position = int(input("Enter position (1-9): "))

                if position < 1 or position > 9:
                    print("Enter a number between 1 and 9.")
                elif board[position - 1] != " ":
                    print("Position already occupied.")
                else:
                    board[position - 1] = "X"
                    break

            except ValueError:
                print("Enter a valid number.")

        if winner("X"):
            show_board()
            print("You Win!")
            break

    # Computer's turn
    else:
        computer_move()
        print("Computer played.")

        if winner("O"):
            show_board()
            print("Computer Wins!")
            break

else:
    show_board()
    print("Draw!")
