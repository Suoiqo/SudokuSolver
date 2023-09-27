


class SudokuSolver():

    def __init__(self, board, schema):
        self.board = board
        self.board_keys = sorted(list(self.board.keys()))
        self.board_schema = schema
        self.qlues = []

    def printElemns(self):
        #Printing all elements of sudoku board
        print(self.board)

    def isEmpty(self, cell):
        #check if value exist in cell if not put 0 in that cell
        if self.board[cell] == '':
            self.board[cell] = 0
            return True
        else:
            return False

    def checkIsValidRow(self, cell):
        #check if value is valid in row
        row_num = cell[-2]
        row_cells = []
        for i in self.board_keys:
            if row_num == i[-2]:
                row_cells.append(i)

        row_values = []
        for one_cell in row_cells:
            if int(self.board[one_cell]) in row_values:
                return False
            else:
                if self.board[one_cell] != 0:
                    row_values.append(int(self.board[one_cell]))
        
        return True


    def checkIsValidColummn(self, cell):
        #check if value is valid in column
        col_num = cell[-1]
        column_cells = []
        for i in self.board_keys:
            if col_num == i[-1]:
                column_cells.append(i)

        col_values = []
        for one_cell in column_cells:
            if int(self.board[one_cell]) in col_values:
                return False
            else:
                if self.board[one_cell] != 0:
                    col_values.append(int(self.board[one_cell]))

            
        return True

    def checkIsValidSquer(self, cell):
        #check if number is valid in 3x3 squer
        for squer in self.board_schema:
            if cell in squer:
                test_squer = squer

        squer_values = []
        for pos in test_squer:
            num = int(self.board[pos])
            if num in squer_values:
                return False
            else:
                if num != 0:
                    squer_values.append(num)
        
        return True
    
    def brutforce(self):
        i = 0
        licznik = 0
        decrise = False

        for pom in self.board.keys():
            if not self.isEmpty(pom):
                self.qlues.append(pom)

        while True:
            licznik += 1
            if i == 81:
                print(licznik)
                return self.board

            if self.board_keys[i] not in self.qlues:
                if self.board[self.board_keys[i]] != 9:
                    decrise = False
                    self.board[self.board_keys[i]] += 1
                else:
                    self.board[self.board_keys[i]] = 0
                    decrise = True
                    i -= 1
                    continue
                if self.checkIsValidColummn(self.board_keys[i]) and self.checkIsValidRow(self.board_keys[i]) and self.checkIsValidSquer(self.board_keys[i]):
                    i += 1
                else:
                    i = i

            elif decrise == True and self.board_keys[i] in self.qlues:
                i -= 1
            else:
                i += 1