import random

from util import argmin_random_tie


def min_conflicts_value(csp, var, current):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(csp.domains[var], key=lambda val: csp.nconflicts(var, val, current))


def min_conflicts(csp, max_steps=100000):
    """Solve a CSP by Hill Climbing on the number of conflicts."""
    """ YOUR CODE HERE """
    # NOTE: similar to coordinate descent (I think)

    import random
    import numpy as np
    from tqdm import tqdm
    from icecream import ic

    def Loss(csp, assignment):
        # CASE1: # conflicted variables
        # return len(csp.conflicted_vars(assignment))

        # CASE2: # conflicted constraints
        return sum(csp.nconflicts(
            var, assignment[var], assignment)
            for var in csp.variables)

    RESTART_TIMES = 40
    best, result, assignment = np.inf, None, {}

    for _ in tqdm(range(RESTART_TIMES)):
        if best == 0:
            break

        # initialize
        assignment = {}
        for var in csp.variables:
            val = random.choice(csp.choices(var, None))
            csp.assign(var, val, assignment)
        loss = Loss(csp, assignment)
        # ic(assignment, loss)

        while True:
            next = None
            for var in csp.conflicted_vars(assignment):
                value = assignment[var]
                val = min_conflicts_value(csp, var, assignment)
                csp.assign(var, val, assignment)
                new_loss = Loss(csp, assignment)
                if new_loss < loss:
                    loss, next = new_loss, (var, val)
                csp.assign(var, value, assignment)
            # print(f"\rloss: {loss:>4d}", end="")

            if next is None:
                break
            csp.assign(*next, assignment)

        if loss < best:
            best, result = ic(loss), assignment.copy()
            # ic(csp.rows, csp.ups, csp.downs)
        for var in csp.variables:
            csp.unassign(var, assignment)

    ic(best)
    # ic(csp.rows, csp.ups, csp.downs)
    for var in result:
        csp.assign(var, result[var], {})
    # csp.display(result)
    return result
