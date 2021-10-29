from .value_order import lcv
from .variable_order import mrv


class Counter():
    def __init__(self, prefix="backtrack") -> None:
        self.cnt = 0
        self.prefix = prefix

    def inc(self):
        self.cnt += 1

    def __str__(self) -> str:
        return f"{self.prefix} times: {self.cnt:>4d}"


def backtracking(
    csp,
    select_unassigned_variable=mrv,
    order_domain_values=lcv
):
    def backtrack(assignment, cnt):
        if len(assignment) == len(csp.variables):
            print(cnt)
            return assignment
        var = select_unassigned_variable(assignment, csp)
        # csp.display(assignment)
        for value in order_domain_values(var, assignment, csp):
            """ YOUR CODE HERE """
            csp.assign(var, value, assignment)
            if csp.nconflicts(var, value, assignment) == 0:
                result = backtrack(assignment, cnt)
                if not result is None:
                    return result
                cnt.inc()
            csp.unassign(var, assignment)
        return None

    result = backtrack({}, Counter())
    assert result is None or csp.goal_test(result)
    return result


def backtracking_with_inference(
    csp,
    inference,
    select_unassigned_variable=mrv,
    order_domain_values=lcv
):
    def backtrack(assignment, cnt):
        """ YOUR CODE HERE """
        if len(assignment) == len(csp.variables):
            print(cnt)
            return assignment
        var = select_unassigned_variable(assignment, csp)
        # csp.display(assignment)
        for value in order_domain_values(var, assignment, csp):
            """ YOUR CODE HERE """
            csp.assign(var, value, assignment)
            if csp.nconflicts(var, value, assignment) == 0:
                removals = csp.suppose(var, value)
                inference(csp, var, value, assignment, removals)
                result = backtrack(assignment, cnt)
                if not result is None:
                    return result
                cnt.inc()
                csp.restore(removals)
            csp.unassign(var, assignment)
        return None

    result = backtrack({},  Counter())
    assert result is None or csp.goal_test(result)
    return result
