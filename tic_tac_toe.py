def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows and Columns
    for i in range(3):
        if all([spot == player for spot in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main Game Code
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    print(f"Player {current_player}, enter row and column (0, 1, or 2):")

    try:
        row = int(input("Row: "))
        col = int(input("Column: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Row and Column must be 0, 1, or 2. Try again.")
            continue
    except ValueError:
        print("Please enter a valid integer for row and column. Try again.")
        continue

    if board[row][col] != " ":
        print("Invalid move! Try again.")
        continue

    board[row][col] = current_player

    # Check Winner
    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break
    
    # Check Draw
    if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # Switch Player
    current_player = "O" if current_player == "X" else "X"