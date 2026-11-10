from typing import Tuple
import clingo, re


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku
    
    def __str__(self) -> str:
        s = "\n"
        count = 1
        for r in range(1, 10):
            for c in range(1, 10):
                s += str(self.sudoku[(r, c)])
                
                if c < 9:
                    if c % 3 == 0:
                        s += "  "  
                if r % 3 == 0:
                    s += "\n\n"  
                else:
                    s += "\n"    
                    
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}

        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {
            (symbol.arguments[0].number, symbol.arguments[1].number): symbol.arguments[2].number
            for symbol in model.symbols(shown=True)
            }
        print(sudoku)

        return cls(sudoku)
