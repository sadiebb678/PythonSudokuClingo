from sudoku_board import Sudoku
import sys, clingo

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for f in files:
            ctl.load("sudoku.lp")
            ctl.load(f)

        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve(on_model=self.on_model)

    def on_model(self, model: clingo.solving.Model):
        self.sudoku_instance = Sudoku.from_model(model)
        return True

    def print_model(self, model, printer ) -> None:
       if self.sudoku_instance:
            # Send the horizontally formatted grid block to stdout
            sys.stdout.write(str(self.sudoku_instance) + "\n")

clingo.application.clingo_main(ClingoApp())