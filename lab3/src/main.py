import argparse
import time

from algorithm.backtracking import backtracking, backtracking_with_inference
from algorithm.hillclimbing import min_conflicts
from algorithm.inference import forward_checking, mac
from algorithm.variable_order import mrv
from classroom import Classroom
from layout import Layout
from nqueens import NQueens
from sudoku import Sudoku


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--algo",
        type=str,
        default="backtrack",
        choices=[
            "backtrack",
            "backtrack+fc", "backtrack+ac3",
            "hill_climbing"
        ]
    )
    parser.add_argument(
        "--layout",
        type=str,
        default="easy_classroom",
        choices=[
            "fail_classroom", "easy_classroom", "harder_classroom", "hardest_classroom",
            "easy_sudoku", "harder_sudoku", "hardest_sudoku",
            "8_nqueens", "10_nqueens"
        ]
    )

    return parser.parse_args()


def main(args):
    # Create problem.
    layout_name, layout_type = args.layout.split("_")

    if layout_type == "classroom":
        layout = Layout(layout_type, layout_name)
        problem = Classroom(layout.matrix.astype(int))
    elif layout_type == "sudoku":
        layout = Layout(layout_type, layout_name)
        problem = Sudoku(layout.matrix)
    elif layout_type == "nqueens":
        problem = NQueens(int(layout_name))
    else:
        raise ValueError

    # Create problem solver.
    if args.algo.startswith("backtrack"):
        tokens = args.algo.split("+")
        if len(tokens) == 1:
            algorithm = backtracking
        elif tokens[1] == "fc":
            def algorithm(p): return backtracking_with_inference(
                p, inference=forward_checking)
        elif tokens[1] == "ac3":
            def algorithm(p): return backtracking_with_inference(
                p, inference=mac)
    elif args.algo == "hill_climbing":
        algorithm = min_conflicts
    else:
        raise ValueError

    # Solve it!
    start = time.time()
    results = algorithm(problem)
    print(f"Time consumption: {time.time() - start:.4f}s")

    # Evaluate your result.
    print("Result:", end=" ")
    if results is not None:
        if problem.goal_test(results):
            print("✔ Success\nSolution:")
            problem.display(results)
        else:
            print("❔ Fail (wrong solution).")
    else:
        print("✘ Fail (no solution found).")


if __name__ == "__main__":
    args = parse_args()
    main(args)
