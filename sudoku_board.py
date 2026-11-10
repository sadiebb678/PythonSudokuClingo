from typing import Tuple
import clingo, re


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku
    
    def __str__(self) -> str:
        s = ""
        count = 1
        for r in range(1, 10):
            for c in range(1, 10):
                s += str(self.sudoku.get((r, c),0))
                
                if c < 9:
                    if c % 3 == 0:
                        s += "  "  
                    else:
                        s += " "
            if r < 9:
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
        sudoku = {}
        for symbol in model.symbols(shown=True):
            # Ensure we are looking at the sudoku predicate with 3 arguments
            if symbol.name == "sudoku" and len(symbol.arguments) == 3:
                r = symbol.arguments[0].number
                c = symbol.arguments[1].number
                val = symbol.arguments[2].number
                sudoku[(r, c)] = val
        return cls(sudoku)
