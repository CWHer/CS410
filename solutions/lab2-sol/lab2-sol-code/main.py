import argparse

from algorithm import SearchAlgorithm
from layout import Layout
from problem import SearchProblem


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate your search algorithms.")
    # parser.add_argument("--algo_name", type=str, default="tiny", choices=["tiny", "dfs", "bfs"])
    # parser.add_argument("--layout_name", type=str, default="tinyMaze", choices=["tinyMaze", "testMaze"])
    parser.add_argument("--algo_name", type=str, default="tiny")
    parser.add_argument("--layout_name", type=str, default="tinyMaze")

    return parser.parse_args()

# def main(args):
#     # Create problem.
#     layout = Layout(args.layout_name)
#     problem = SearchProblem(layout=layout)
#     print("Layout:")
#     layout.display()
#     print()

#     # Create problem solver.
#     algorithm = SearchAlgorithm(args.algo_name)

#     # Solve it!
#     actions = algorithm(problem)

#     # Evaluate your result.
#     print("Result:")
#     res = problem.eval_actions(actions)
#     if res["success"]:
#         print(f"✔ Successfully reach the goal (cost={res['cost']}).")
#     else:
#         print("✘ Fail to reach the goal.")

def main(args):
    # Create problem.
    layout = Layout(args.layout_name)
    problem = SearchProblem(layout=layout)
    print("Layout:")
    layout.display()
    print()

    # Create problem solver.
    algorithm = SearchAlgorithm(args.algo_name)

    # Solve it!
    res = algorithm(problem)

    # Evaluate your result.
    print("Result:")
    print(res)

if __name__ == "__main__":
    args = parse_args()
    main(args)
