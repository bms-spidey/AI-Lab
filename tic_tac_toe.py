import math

# Set up the game board as a list
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Define a function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Define a function to check if a specific player has won
def check_win(player):
    return (
        (board[0] == board[1] == board[2] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[0] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    )

# Define a function to check the current game state
def check_game_over():
    if check_win("X") or check_win("O"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"

# The Minimax Algorithm
def minimax(is_maximizing):
    # Base cases: evaluate terminal states
    if check_win("O"):  # AI wins
        return 1
    if check_win("X"):  # Human wins
        return -1
    if "-" not in board:  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(False)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(True)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

# Function to calculate the AI's best move
def get_ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Define a function to handle a player's turn
def take_turn(player):
    print(player + "'s turn.")
    
    if player == "X":
        # Human turn logic with input validation
        position = input("Choose a position from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        
        while board[position] != "-":
            position = int(input("Position already taken. Choose a different position: ")) - 1
            
        board[position] = player
    else:
        # AI turn logic
        print("AI is thinking...")
        position = get_ai_move()
        board[position] = player
        
    print_board()

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"  # X is human, O is AI
    game_over = False
    
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        
        if game_result == "win":
            if current_player == "O":
                print("AI (O) wins! Better luck next time.")
            else:
                print("X wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
