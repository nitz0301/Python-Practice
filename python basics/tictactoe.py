import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_layout(positions: list):
    clear()
    print("\nWelcome to Tic Tac Toe by Nishith Sharma\n")
    print("Below are the latest positions\n")
    
    for row in positions:
        line = ''
        col = 1
        for item in row:
            if col % 3 != 0:
                line = line + f"{item} | "
            else:
                line = line + f"{item}"
            col += 1
        print(line)
        
def check_win(taken_pos: list, symb: str) -> bool:
    if taken_pos[0] == [symb,symb,symb] or taken_pos[1] == [symb,symb,symb] or taken_pos[2] == [symb,symb,symb]:
        return True
    elif taken_pos[0][0] == symb and taken_pos[1][1] == symb and taken_pos[2][2] == symb:
        return True
    elif taken_pos[0][2] == symb and taken_pos[1][1] == symb and taken_pos[2][0] == symb:
        return True
    elif taken_pos[0][0] == symb and taken_pos[1][0] == symb and taken_pos[2][0] == symb:
        return True
    elif taken_pos[0][1] == symb and taken_pos[1][1] == symb and taken_pos[2][1] == symb:
        return True
    elif taken_pos[0][2] == symb and taken_pos[1][2] == symb and taken_pos[2][2] == symb:
        return True
    else:
        return False
    
win = False
player = 1
valid_str = ['1','2','3','4','5','6','7','8','9']
taken_positions = []
layout_positions = [[1,2,3],[4,5,6],[7,8,9]]
current_pos = 0
players = []

# Game initialize
clear()
players.append(input("Player 1, Enter your name: "))
players.append(input("Player 2, Enter your name: "))


print_layout(layout_positions)

while(win == False):
    pos_str = input(f"\n{players[player - 1]}, what position do you want to play? ")
    if pos_str in valid_str:
        if pos_str in taken_positions:
            print("This position is taken, retry")
        else:
            if player == 1:
                symbol = 'X'
            else:
                symbol = 'O'
            
            if int(pos_str) < 4:
                layout_positions[0][int(pos_str) % 4 - 1] = symbol
                taken_positions.append(pos_str)
            elif int(pos_str) < 7:
                layout_positions[1][int(pos_str) % 7 - 4] = symbol
                taken_positions.append(pos_str)
            else:
                layout_positions[2][int(pos_str) % 10 - 7] = symbol
                taken_positions.append(pos_str)
            print_layout(layout_positions)
            current_pos += 1
            if check_win(layout_positions, symbol):
                print(f"\n{players[player -1]} wins, Congratulations !\n")
                win = True
            else: 
                if (current_pos > 8):
                    print("\nMatch draw. Game Over !")
                    win = True
            if player == 1:
                player = 2
            else:
                player = 1
    else:
        print("Invalid position, retry")
            