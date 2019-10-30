class TaTeTi():
    def __init__(self, board=None):
        if not board:
            board = [' ' for _ in range(9)]
        self.board = board

    def full(self):
        for i in range(9):
            if self.board[i] == " ":
                return False
        return True

    def win(self):
        for i in range(9):
            if i == 0 or i == 3 or i == 6:
                if self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2] and self.board[i] != ' ':
                    return True
        if self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[6] != ' ':
            return True
        elif self.board[1] == self.board[4] and self.board[7] == self.board[1] and self.board[1] != ' ':
            return True
        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' ':
            return True
        elif self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[0] != ' ':
            return True
        elif self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[2] != ' ':
            return True
        else:
            return False

    def validate(self, position):
        return self.board[position - 1] == " "

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position-1] = piece
        else:
            raise Exception

    def draw_board(self):
        self.display = "\n"
        for i in range(9):
            if self.board[i] != " ":
                self.display += " " + self.board[i] + " "

            else:
                self.display += " " + str(1+i) + " "

            if i == 2 or i == 5:
                self.display += "\n---+---+---\n"

            elif i == 8:
                self.display += "\n"

            else:
                self.display += "|"

        return self.display
