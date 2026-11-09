import sys, clingo

class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        for f in files:
            ctl.load("sudoku.lp")
            ctl.load(f)

        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()

    def print_model(self, model: Model, printer: Callable[[], None]) -> None:
        symbols = model.symbols(shown=True)
        sorted_symbols = sorted(symbols)
        print(" ".join(map(str, sorted_symbols)))
        
clingo.application.clingo_main(ClingoApp())