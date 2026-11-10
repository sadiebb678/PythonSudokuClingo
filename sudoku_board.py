from typing import Tuple
import clingo, re


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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
