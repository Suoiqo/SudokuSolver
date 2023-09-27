from threads import init_threads
from SudokuSolver import SudokuSolver

web_output_queue, web_input_queue = init_threads()
#prepering board schema to future tests
board_schema = [[], [], [], [], [], [], [], [], []]
i = 0
j = 0
for x in range(9):
    if x % 3 == 0 and x != 0:
        i += 3
    j = 0
    for y in range(9):
        if y % 3 == 0 and y != 0:
            j += 1
        board_schema[i + j].append('pole' + str(x) + str(y))


if __name__ == '__main__':
    while True:
        if not web_output_queue.empty():
            sudoku_bord = web_output_queue.get()
            for k in sudoku_bord.keys():
                sudoku_bord[k] = sudoku_bord[k][0]
            x = SudokuSolver(sudoku_bord, board_schema)
            answer = x.brutforce()
            if answer:
                web_input_queue.put(answer)            