from threads import init_threads
from SudokuSolver import SudokuSolver

def main():
    #Initialize web server and queues
    web_output_queue, web_input_queue = init_threads()
    i = 1
    while True:
        try:
            #Check if there's Sudoku board data in the output queue
            if not web_output_queue.empty():
                sudoku_board = web_output_queue.get()

                #Extract 'value' from the response and convert it to int and if is empty change it to 0
                #(the user output will always be a dictionary - 'yx': ['value'], empty cell will have empty string)
                for k in sudoku_board.keys():
                    sudoku_board[k] = int(sudoku_board[k][0]) if sudoku_board[k][0] != '' else 0
                    
                #Solve Sudoku using SudokuSolver
                sudoku = SudokuSolver(sudoku_board)
                answer = sudoku.backtracking_algorithm()

                #Put the answer in the input queue to send back to the web server
                web_input_queue.put(answer)
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    '''
    Main loop of program.
    Checking if there is sudoku board data in output queue from website and take first elemet.
    Initialization of SudokuSolver class and use backtracking_algorithm method to solve sudoku.
    Result is put in input queue.
    '''
    main()

