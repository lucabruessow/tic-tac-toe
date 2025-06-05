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
            return "finished"
        if self.cells[1][0] == self.cells[1][1] == self.cells[1][2] and not " ":
            return "finished"
        if self.cells[2][0] == self.cells[2][1] == self.cells[2][2] and not " ":
            return "finished"
        
        # all vertical options
        if self.cells[0][0] == self.cells[1][0] == self.cells[2][0] and not " ":
            return "finished"
        if self.cells[0][1] == self.cells[1][1] == self.cells[2][1] and not " ":
            return "finished"
        if self.cells[0][2] == self.cells[1][2] == self.cells[2][2] and not " ":
            return "finished"

        # all diagonal options
        if self.cells[0][0] == self.cells[1][1] == self.cells [2][2] and not " ":
            return "finished"
        if self.cells[0][2] == self.cells[1][1] == self.cells [2][0] and not " ":
            return "finished"

        # draw
        if " " not in self.cells[0] and " " not in self.cells[1] and " " not in self.cells[2]:
            return "draw"

board_cells = []

board = Board(board_cells)

print(board)