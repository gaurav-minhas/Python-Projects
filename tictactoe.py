def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")

        # Get valid row and column from current player
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if board[row][col] == " ":
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 2.")

        # Place the player's marker on the board
        board[row][col] = current_player
        print_board(board)

        # Check if the current player wins
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie)
        if is_board_full(board):
            print("It's a tie!")
            break

        # Switch turns
        current_player = "O" if current_player == "X" else "X"

    print("Game Over.")

if __name__ == "__main__":
    main()
1