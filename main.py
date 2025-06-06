import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board:
    def __init__(self, cells):
        
        self.cells = [[" ", " ", " ",],
                      [" ", " ", " ",],
                      [" ", " ", " ",]]

    def __str__(self):
        return (f"   A   B   C\n"
                f"1  {self.cells[0][0]}   {self.cells[0][1]}   {self.cells[0][2]}\n"
                f"2  {self.cells[1][0]}   {self.cells[1][1]}   {self.cells[1][2]}\n"
                f"3  {self.cells[2][0]}   {self.cells[2][1]}   {self.cells[2][2]}")
    
    def is_game_finished(self):
        win_conditions = [
            # horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (2, 2)],
            [(2, 0), (2, 1), (2, 2)],

            #vertical
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            # diagonal
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for line in win_conditions:
            a = line[0]
            b = line[1]
            c = line[2]

            if self.cells[a[0]][a[1]] == self.cells[b[0]][b[1]] == self.cells[c[0]][c[1]] and self.cells[a[0]][a[1]] != " ":
                return self.cells[a[0]][a[1]]

        """ # all horizontal options
        if self.cells[0][0] == self.cells[0][1] == self.cells[0][2] and self.cells[0][0] != " ":
            return True
        if self.cells[1][0] == self.cells[1][1] == self.cells[1][2] and self.cells[1][0] != " ":
            return True
        if self.cells[2][0] == self.cells[2][1] == self.cells[2][2] and self.cells[2][0] != " ":
            return True
        
        # all vertical options
        if self.cells[0][0] == self.cells[1][0] == self.cells[2][0] and self.cells[0][0] != " ":
            return True
        if self.cells[0][1] == self.cells[1][1] == self.cells[2][1] and self.cells[0][1] != " ":
            return True
        if self.cells[0][2] == self.cells[1][2] == self.cells[2][2] and self.cells[0][2] != " ":
            return True

        # all diagonal options
        if self.cells[0][0] == self.cells[1][1] == self.cells [2][2] and self.cells[0][0] != " ":
            return True
        if self.cells[0][2] == self.cells[1][1] == self.cells [2][0] and self.cells[2][0] != " ":
            return True

        # draw
        if " " not in self.cells[0] and " " not in self.cells[1] and " " not in self.cells[2]:
            return True
        
        else:
            return False """

    def game_start(self, player1, player2):
        active_round = 0
        while not self.is_game_finished() and active_round < 9:
            clear_screen()
            print(board)
            print(player1.active)
            
            if player1.active:
                player1.make_move(self, player2)
                active_round += 1

            elif player2.active:
                player2.make_move(self, player1)
                active_round += 1
        
        result = board.is_game_finished()
        print(result)
        if result == "X":
            print(f"{player1.name} has won.")
        elif result == "O":
            print(f"{player2.name} has won.")
        else:
            print("Draw.")
        


class Player:
    def __init__(self, name, sign, active):
        
        self.name = name
        self.sign = sign
        self.active = active

    def __str__(self):
        return f"{self.name}"
    
    def make_move(self, board, next_player):
        inp = ""
        while inp.lower not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
            inp = input(f"\n{self.name}, make your move: ").lower()
            if inp.lower() not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
                print("Wrong input. Choose an existing cell.")
                time.sleep(2)
                continue

            # change board column a
            if inp == "a1" and board.cells[0][0] == " ":
                board.cells[0][0] = self.sign
                self.active = False
                next_player.active = True
                break            
            if inp == "a2" and board.cells[1][0] == " ":
                board.cells[1][0] = self.sign
                self.active = False
                next_player.active = True
                break
            if inp == "a3" and board.cells[2][0] == " ":
                board.cells[2][0] = self.sign
                self.active = False
                next_player.active = True
                break
            
            # change board column b
            if inp == "b1" and board.cells[0][1] == " ":
                board.cells[0][1] = self.sign
                self.active = False
                next_player.active = True
                break
            if inp == "b2" and board.cells[1][1] == " ":
                board.cells[1][1] = self.sign
                self.active = False
                next_player.active = True
                break
            if inp == "b3" and board.cells[2][1] == " ":
                board.cells[2][1] = self.sign
                self.active = False
                next_player.active = True
                break

            # change board column c
            if inp == "c1" and board.cells[0][2] == " ":
                board.cells[0][2] = self.sign
                self.active = False
                next_player.active = True
                break
            if inp == "c2" and board.cells[1][2] == " ":
                board.cells[1][2] = self.sign
                self.active = False
                next_player.active = True
                break
            if inp == "c3" and board.cells[2][2] == " ":
                board.cells[2][2] = self.sign
                self.active = False
                next_player.active = True
                break
            
            else:
                print("Cell already taken. Choose another one.")
                inp = ""



# start program
clear_screen()

board_cells = []

player1 = Player(input("Type the name of player 1: "), "X", True)
player2 = Player(input("Type the name of Player 2: "), "O", False)

board = Board(board_cells)

board.game_start(player1, player2)
result = board.is_game_finished()