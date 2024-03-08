# Author: Reyad Yossef Ebrahim
# ID: 20230143
# Version: v3.0
# Date: 28/2/2024

import random  # Import the random module to generate random numbers for player selection

# Function to initialize the game board with empty cells represented by 0
def initialize_board():
    return [0] * 16

# Function to print the game board
def print_board(board):
    for i in range(0, 16, 4):
        # Print each row of the board with cells separated by spaces
        print(" ".join(str(cell) if cell != 0 else "_" for cell in board[i:i+4]))

# Function to check if two boxes are adjacent
def is_adjacent(box1, box2):
    return abs(box1 - box2) == 1 or abs(box1 - box2) == 4

# Function to check if a box is empty
def is_empty(board, box):
    return board[box - 1] == 0

# Function to place a block on the board
def place_block(board, box1, box2, player):
    if is_adjacent(box1, box2) and is_empty(board, box1) and is_empty(board, box2):
        # Fill the selected boxes with 'X' to represent the player's move
        board[box1 - 1] = board[box2 - 1] = 'X'
        return True
    return False

# Function to switch between players
def switch_player(player):
    return 2 if player == 1 else 1

# Function to check if the board is full
def is_board_full(board):
    return all(cell != 0 for cell in board)

# Function to check if there are adjacent empty boxes on the board
def has_adjacent_boxes(board):
    for i in range(1, 17):
        if board[i - 1] == 0 and (
            (i % 4 != 0 and board[i] == 0) or
            (i % 4 != 1 and board[i - 2] == 0) or            
            (i > 4 and board[i - 5] == 0) or
            (i < 13 and board[i + 3] == 0)
        ):
            return True
    return False

# Function to print the welcome message and game instructions
def print_welcome_message():
    print("Welcome to the Two Box Game!")
    print("In this game, you and your opponent take turns placing blocks on a 4x4 grid.")
    print("Each turn, you'll choose two adjacent empty boxes to place your block.")
    print("The goal is to strategically place your blocks to prevent your opponent from making a move.")
    print("The game ends when the grid is full or when no adjacent empty boxes are available.")

# Function to start and control the game
def play_game():
    print_welcome_message()  # Print the welcome message and game instructions
    while True:
        choice = input("Press 'S' to start the game or 'E' to exit: ").upper()  # Prompt the player to start or exit
        if choice == 'S':  # If the player chooses to start the game
            game_board = initialize_board()  # Initialize the game board
            current_player = random.randint(1, 2)  # Randomly select the starting player
            last_player = None

            while not is_board_full(game_board):  # Continue the game until the board is full
                print_board(game_board)  # Print the current state of the game board
                print("Player", current_player)  # Print the current player's turn
                box1 = int(input("Enter the number of the first box (1-16): "))  # Prompt the player to select the first box
                box2 = int(input("Enter the number of the second box (1-16): "))  # Prompt the player to select the second box
                
                if box1 < 1 or box1 > 16 or box2 < 1 or box2 > 16:  # Validate the selected box numbers
                    print("Invalid box number. Please enter a number between 1 and 16.")
                    continue
                
                if place_block(game_board, box1, box2, current_player):  # Place a block on the board if the move is valid
                    if has_adjacent_boxes(game_board):  # Check if there are adjacent empty boxes for the next move
                        current_player = switch_player(current_player)  # Switch to the next player's t
