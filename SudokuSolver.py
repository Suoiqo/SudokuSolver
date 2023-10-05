
class SudokuSolver():
    '''
    This is a class for sudoku solver with backtracking method.
    Takes input from the user and return complited sudoku board with those preconditions.
    '''

    def __init__(self, board):
        self.board = board
        self.board_keys = sorted(list(self.board.keys()))
        self.board_schema = self.init_schema()
        self.qlues = []

    def init_schema(self):
        '''
        Prepering board schema for future tests.
        Every list contains 3x3 squers position of the board
        '''
        board_schema = [[] for _ in range(9)]
        for y in range(9):
            for x in range(9):
                board_schema[(y //3) * 3 + x // 3].append(str(y) + str(x))

        return board_schema

    def printElemns(self):
        #Printing all elements of sudoku board
        print(self.board)

    def checkIsValid(self, cell):
        '''
        Check if number is valid for given cell
        '''
        cell_value = self.board[cell]
        row_num, col_num = int(cell[-2]), int(cell[-1])

        #Check if number is valid in column
        if cell_value in [self.board[f'{i}{col_num}'] for i in range(9) if i != row_num]:
            return False
            
        #Check if number is valid in row
        if cell_value in [self.board[f'{row_num}{i}'] for i in range(9) if i != col_num]:
            return False
                   
        #Check if number is valid in 3x3 squer
        square_num = (row_num // 3) * 3 + (col_num // 3)
        for pos in self.board_schema[square_num]:
            if cell != pos and cell_value == self.board[pos]:
                return False
                
        return True

    
    def backtracking_algorithm(self):
        '''
        Main loop of backtracking algorithm
        '''
        #Varible pointing to current cell in slef.board_schema
        position = 0
        licznik = 0 #counter for number of iterations

        #Adding filled by user cell to self.qlues
        for k in self.board.keys():
            if self.board[k] != 0:
                self.qlues.append(k)

        while True:
            licznik += 1

            #Ending loop after last cell
            if position >= 81:
                print(licznik)
                return self.board

            #Ending loop if its counting to long or decrease position to negative values
            #Some sudoku boards cannot ve solved using backtracking method or initial values are in wrong positions
            if licznik >= 500000 or position < 0:
                print(licznik)
                return ''
            
            #Check if current position is not in self.qluese and increse cell value if value in cell is less then 9
            if self.board_keys[position] not in self.qlues:
                if self.board[self.board_keys[position]] != 9:
                    self.board[self.board_keys[position]] += 1
                else:
                    #If value in cell is greater then 9, reset value and decrease position
                    self.board[self.board_keys[position]] = 0
                    position -= 1
                    #Decrease position if positoion is in self.qlues and skip rest of program
                    while self.board_keys[position] in self.qlues:
                        position -= 1
                    continue
                
                #Check if value is valid in current posirion
                if self.checkIsValid(self.board_keys[position]):
                    position += 1 #move to next position
                else:
                    position = position #value is invalid, stay in current position

            else:
                position += 1 #position is in self.clues move to next position