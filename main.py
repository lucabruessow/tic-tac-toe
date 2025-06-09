import time
import os
import random
import copy

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
    
    def is_draw(self):
        for row in self.cells:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def is_game_finished(self):
        win_conditions = [
            # horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
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

        if self.is_draw():
            return "draw"
            
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
        while not self.is_game_finished():
            clear_screen()
            print(board)
            
            if player1.active:
                player1.make_move(self, player2)

            elif player2.active:
                player2.make_move(self, player1)
        
        # print with all moves on board
        clear_screen()
        print(board)

        # print winner
        result = board.is_game_finished()
        if result == "X":
            print(f"{player1.name} has won.")
            time.sleep(2)
        elif result == "O":
            print(f"{player2.name} has won.")
            time.sleep(2)
        elif result == "draw":
            print("Draw.")
            time.sleep(2)
    
    def get_available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == " ":
                    moves.append((i, j))
        return moves
    

class Player:
    def __init__(self, name, sign, active, ai):
        
        self.name = name
        self.sign = sign
        self.active = active
        self.ai = ai
    
    def make_move(self, board, next_player):
        inp = ""
        while inp.lower not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]:
            if not self.ai:
                inp = input(f"\n{self.name}, make your move: \n").lower()    
            else:
                inp = self.ai_best_move_generator(board)
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
            elif inp == "a2" and board.cells[1][0] == " ":
                board.cells[1][0] = self.sign
                self.active = False
                next_player.active = True
                break
            elif inp == "a3" and board.cells[2][0] == " ":
                board.cells[2][0] = self.sign
                self.active = False
                next_player.active = True
                break
            
            # change board column b
            elif inp == "b1" and board.cells[0][1] == " ":
                board.cells[0][1] = self.sign
                self.active = False
                next_player.active = True
                break
            elif inp == "b2" and board.cells[1][1] == " ":
                board.cells[1][1] = self.sign
                self.active = False
                next_player.active = True
                break
            elif inp == "b3" and board.cells[2][1] == " ":
                board.cells[2][1] = self.sign
                self.active = False
                next_player.active = True
                break

            # change board column c
            elif inp == "c1" and board.cells[0][2] == " ":
                board.cells[0][2] = self.sign
                self.active = False
                next_player.active = True
                break
            elif inp == "c2" and board.cells[1][2] == " ":
                board.cells[1][2] = self.sign
                self.active = False
                next_player.active = True
                break
            elif inp == "c3" and board.cells[2][2] == " ":
                board.cells[2][2] = self.sign
                self.active = False
                next_player.active = True
                break
            
            elif not self.ai:
                print("Cell already taken. Choose another one.")
                inp = ""

    def ai_random_move_generator(self):
        list_of_column = ["a", "b", "c"]
        list_of_row = ["1", "2", "3"]

        return random.choice(list_of_column) + random.choice(list_of_row)
    
    def simulate(self, board, current_sign):
        winner = board.is_game_finished()
        if winner:
            if winner == self.sign: return 1
            if winner == "draw": return 0
            return -1
        
        total = 0
        for (i, j) in board.get_available_moves():
            copy_board = copy.deepcopy(board)
            copy_board.cells[i][j] = current_sign
            next_sign = "O" if current_sign == "X" else "X"
            total += self.simulate(copy_board, next_sign)
        return total

    def ai_best_move_generator(self, board):
        best_move = None
        best_score = -999

        for move in board.get_available_moves():
            i = move[0]
            j = move[1]

            test_board = copy.deepcopy(board)
            test_board.cells[i][j] = self.sign

            score = self.simulate(test_board, "X")

            if score > best_score:
                best_score = score
                best_move = (i, j)
        
        convert_to_string = {
            (0, 0): "a1", (1, 0): "a2", (2, 0): "a3",
            (0, 1): "b1", (1, 1): "b2", (2, 1): "b3",
            (0, 2): "c1", (1, 2): "c2", (2, 2): "c3"
        }

        return convert_to_string[best_move]


# start program
while True:
    clear_screen()
    print("      Tic Tac Toe\n"
        "------------------------\n"
        "[1] Start with 2 player\n"
        "[2] Start with (good) AI\n"
        "[3] Exit Game\n")

    inp = input("Type 1, 2 or 3: ")

    if inp == "1":
        clear_screen()
        board_cells = []
        player1 = Player(input("Type the name of player 1: "), "X", True, False)
        player2 = Player(input("Type the name of Player 2: "), "O", False, False)
        board = Board(board_cells)

        board.game_start(player1, player2)

    elif inp == "2":
        clear_screen()
        board_cells = []
        player1 = Player(input("Type the name of player 1: "), "X", True, False)
        ai = Player("AI", "O", True, True)
        board = Board(board_cells)

        board.game_start(player1, ai)

    elif inp == "3":
        print("Goodbye.")
        break

    else:
        print("Wrong input. Type 1, 2 or 3.")
        time.sleep(2)