# Sudoku Solver

This is a simply Python program for solving Sudoku puzzles using a backtracking algorithm. It takes input from a user through a web interface hosted on `localhost:8000` and returns a completed Sudoku board based on the provided preconditions.

## Sudoku Solver Class

The `SudokuSolver` class is responsible for solving Sudoku puzzles. It has the following methods:

- `__init__(self, board)`: Initializes the solver with the Sudoku board.
- `init_schema(self)`: Prepares the board schema for future tests, grouping cells into 3x3 squares.
- `printElemns(self)`: Prints all elements of the Sudoku board.
- `checkIsValid(self, cell)`: Checks if a number is valid for a given cell.
- `backtracking_algorithm(self)`: The main loop of the backtracking algorithm for solving Sudoku puzzles.

## HTTP Server

The program uses a basic HTTP server to host a web interface for input and display the solved Sudoku puzzle. It includes a custom `RequestHandler` class that handles both GET and POST requests.

## Usage

1. Start the program, and the HTTP server will be available at `http://localhost:8000`.
2. Access the web interface in your browser to input the Sudoku puzzle.
3. After submitting the puzzle, the program will solve it and display the completed Sudoku board on the `/answer.html` page.

Please note that this program uses a simple backtracking algorithm and may not be suitable for extremely complex Sudoku puzzles or those with multiple solutions.
