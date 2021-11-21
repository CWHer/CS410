import argparse
import time

from problem.GridMDP import getEnv

from algorithm.value_iteration import value_iteration, best_policy
from algorithm.policy_iteration import policy_iteration

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--algo",
        type=str,
        default="value_iteration",
        choices=[
            "value_iteration",
            "policy_iteration"
        ]
    )

    parser.add_argument(
        "--problem",
        type=str,
        default="grid_mdp",
        choices=[
            "grid_mdp"
        ]
    )

    parser.add_argument(
        "--blue_state_reward",
        type = float,
        default = -0.01,
        choices = [
            -0.01, -0.4, -2.0
        ],
        help = "the reward of the blue state in the 2-dim grid mdp"
    )

    return parser.parse_args()

def main(args):
    problem, algo = args.problem, args.algo

    # Create problem.
    if problem == "grid_mdp":
        problem = getEnv(args.blue_state_reward)
    else:
        raise ValueError

    # Create problem solver.
    if algo == "value_iteration":
        algo = value_iteration
    elif algo == "policy_iteration":
        algo = policy_iteration
    else:
        raise ValueError

    # Solve it!
    start = time.time()
    utilities, policy = algo(problem)
    policy_visualization = problem.to_arrows(policy)
    pv = ''
    for i in policy_visualization:
        for j in range(len(i)):
            if i[j] == None:
                i[j] = 'N'
        pv += ' '.join(i) + '\n'
    print(f"Time consumption: {time.time() - start:.4f}s")

    # Your result.
    print("Result:\nutilities found by {} is\n{}\n policy found by {} is\n{}".format(args.algo, utilities, args.algo, pv))
    

if __name__ == "__main__":
    args = parse_args()
    main(args)
