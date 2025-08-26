import os
from typing import List, Union


def clear() -> None:
    """
    Clear the console screen.

    Uses the appropriate system command depending on the operating system:
    - 'cls' for Windows
    - 'clear' for Linux/macOS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_layout(positions: List[List[Union[int, str]]]) -> None:
    """
    Print the current Tic Tac Toe board layout.

    Args:
        positions (List[List[Union[int, str]]]): 
            A 3x3 matrix representing the board. 
            Each element is either a number (available position) or a symbol ('X' or 'O').
    """
    clear()
    print("\nWelcome to Tic Tac Toe by Nishith Sharma\n")
    print("Below are the latest positions\n")

    # Print each row with separators
    for row in positions:
        line = ''
        col = 1
        for item in row:
            # Add ' | ' separator for first two columns
            if col % 3 != 0:
                line = line + f"{item} | "
            else:
                line = line + f"{item}"
            col += 1
        print(line)


def check_win(taken_pos: List[List[Union[int, str]]], symb: str) -> bool:
    """
    Check whether the given symbol has won the game.

    Args:
        taken_pos (List[List[Union[int, str]]]): 
            A 3x3 matrix representing the board.
        symb (str): 
            The symbol to check ('X' or 'O').

    Returns:
        bool: True if the symbol has a winning line (row, column, or diagonal), otherwise False.
    """
    # Check horizontal rows
    if taken_pos[0] == [symb, symb, symb] or taken_pos[1] == [symb, symb, symb] or taken_pos[2] == [symb, symb, symb]:
        return True
    # Check main diagonal
    elif taken_pos[0][0] == symb and taken_pos[1][1] == symb and taken_pos[2][2] == symb:
        return True
    # Check anti-diagonal
    elif taken_pos[0][2] == symb and taken_pos[1][1] == symb and taken_pos[2][0] == symb:
        return True
    # Check vertical columns
    elif taken_pos[0][0] == symb and taken_pos[1][0] == symb and taken_pos[2][0] == symb:
        return True
    elif taken_pos[0][1] == symb and taken_pos[1][1] == symb and taken_pos[2][1] == symb:
        return True
    elif taken_pos[0][2] == symb and taken_pos[1][2] == symb and taken_pos[2][2] == symb:
        return True
    else:
        return False


# Game state variables
win: bool = False  # Track if game has ended
player: int = 1  # Current player (1 or 2)
valid_str: List[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Valid board positions
taken_positions: List[str] = []  # Track already used positions
layout_positions: List[List[Union[int, str]]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Initial board
current_pos: int = 0  # Number of moves made
players: List[str] = []  # Player names

# Initialize game
clear()
players.append(input("Player 1, Enter your name: "))
players.append(input("Player 2, Enter your name: "))

print_layout(layout_positions)

# Game loop
while not win:
    # Ask current player for position
    pos_str = input(f"\n{players[player - 1]}, what position do you want to play? ")

    # Validate input
    if pos_str in valid_str:
        if pos_str in taken_positions:
            print("This position is taken, retry")
        else:
            # Assign symbol based on player
            if player == 1:
                symbol = 'X'
            else:
                symbol = 'O'

            # Update board depending on chosen position
            if int(pos_str) < 4:  # First row
                layout_positions[0][int(pos_str) % 4 - 1] = symbol
                taken_positions.append(pos_str)
            elif int(pos_str) < 7:  # Second row
                layout_positions[1][int(pos_str) % 7 - 4] = symbol
                taken_positions.append(pos_str)
            else:  # Third row
                layout_positions[2][int(pos_str) % 10 - 7] = symbol
                taken_positions.append(pos_str)

            # Refresh board
            print_layout(layout_positions)
            current_pos += 1

            # Check win condition
            if check_win(layout_positions, symbol):
                print(f"\n{players[player - 1]} wins, Congratulations!\n")
                win = True
            else:
                # If 9 moves are done and no win → draw
                if current_pos > 8:
                    print("\nMatch draw. Game Over!")
                    win = True

            # Switch player
            player = 2 if player == 1 else 1
    else:
        print("Invalid position, retry")
