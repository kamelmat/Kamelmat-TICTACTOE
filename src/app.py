def new_game():
    # Initialize the game board as a 3x3 matrix filled with spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # X always starts
    return board, current_player


def print_board(board):
    # Print the current state of the board
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def play(row, col, board, current_player):
    # Place the current player's mark at the specified position
    if board[row][col] == ' ':
        board[row][col] = current_player
        return True
    return False


def check_for_winner(board):
    # Check all win conditions: rows, columns, and diagonals
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != ' ':
            return board[0][j]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def is_board_full(board):
    # Check if there are any empty spaces left on the board
    for row in board:
        if ' ' in row:
            return False
    return True


def main():
    board, current_player = new_game()
    while True:
        print_board(board)
        user_input = input(
            f"Player {current_player}, enter your move (row col) or 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break
        try:
            row, col = map(int, user_input.split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print(
                    "Invalid input, please enter row and column as numbers between 0 and 2.")
                continue
            if play(row, col, board, current_player):
                winner = check_for_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    if input("Play again? (y/n): ").lower() == 'y':
                        board, current_player = new_game()
                        continue
                    else:
                        break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    if input("Play again? (y/n): ").lower() == 'y':
                        board, current_player = new_game()
                        continue
                    else:
                        break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input, please enter row and column as x y.")


if __name__ == "__main__":
    main()
