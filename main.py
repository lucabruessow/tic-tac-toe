import time

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
    
    def game_finished(self):
        # all horizontal options
        if self.cells[0][0] == self.cells[0][1] == self.cells[0][2] and not " ":
            return True
        if self.cells[1][0] == self.cells[1][1] == self.cells[1][2] and not " ":
            return True
        if self.cells[2][0] == self.cells[2][1] == self.cells[2][2] and not " ":
            return True
        
        # all vertical options
        if self.cells[0][0] == self.cells[1][0] == self.cells[2][0] and not " ":
            return True
        if self.cells[0][1] == self.cells[1][1] == self.cells[2][1] and not " ":
            return True
        if self.cells[0][2] == self.cells[1][2] == self.cells[2][2] and not " ":
            return True

        # all diagonal options
        if self.cells[0][0] == self.cells[1][1] == self.cells [2][2] and not " ":
            return True
        if self.cells[0][2] == self.cells[1][1] == self.cells [2][0] and not " ":
            return True

        # draw
        if " " not in self.cells[0] and " " not in self.cells[1] and " " not in self.cells[2]:
            return True
        
        else:
            return False


class Player:
    def __init__(self, name, sign):
        
        self.name = name
        self.sign = sign

    def __str__(self):
        return f"{self.name}"
    
    def make_move(self, board):
        inp = ""
        while inp.lower not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
            inp = input("Choose a cell: ")
            if inp.lower not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
                print("Wrong input. Choose an existing cell.")
                time.sleep(2)

        # change board column a
        if inp == "a1":
            board.cells[0][0] = self.sign
        if inp == "a2":
            board.cells[1][0] = self.sign
        if inp == "a3":
            board.cells[2][0] = self.sign
        
        # change board column b
        if inp == "b1":
            board.cells[0][1] = self.sign
        if inp == "b2":
            board.cells[1][1] = self.sign
        if inp == "b3":
            board.cells[2][1] = self.sign

        # change board column c
        if inp == "c1":
            board.cells[0][2] = self.sign
        if inp == "c2":
            board.cells[1][2] = self.sign
        if inp == "c3":
            board.cells[2][2] = self.sign



board_cells = []
player1 = Player(input("Type the name of player 1: "), "X")
player2 = Player(input("Type the name of Player 2: "), "O")

board = Board(board_cells)

print(board)