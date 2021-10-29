import numpy as np

from csp import CSP
from util import count


class Classroom(CSP):
    def __init__(self, ini_seats):
        self.dict = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.ini_seats = ini_seats
        self.n, self.m = len(ini_seats), len(ini_seats[0])
        self.friends = self.gen_friends()

        self.variables = [(i, j) for i in range(self.n) for j in range(self.m)]
        self.domains = {v: list(range(1, self.n*self.m+1))
                        for v in self.variables}
        self.curr_domains = None
        self.neighbors = {v: set(self.variables) -
                          set([v]) for v in self.variables}
        self.constraints = self._classroom_conflict
        self.nassigns = 0

    def _classroom_conflict(self, var1, val1, var2, val2):
        """ YOUR CODE HERE """
        # NOTE: none of these students are adjacent to his/her friends
        return (not self._is_adjacent(var1, var2)
                or not self._is_friend(val1, val2))

    def gen_friends(self):
        res = dict()
        for i in range(self.n):
            for j in range(self.m):
                val = self.ini_seats[i][j]
                res[val] = []
                for k in range(4):
                    ni, nj = i+self.dict[k][0], j+self.dict[k][1]
                    if (0 <= ni and ni < self.n) and (0 <= nj and nj < self.m):
                        res[val].append(self.ini_seats[ni][nj])
        return res

    @staticmethod
    def _is_adjacent(var1, var2):
        return abs(var1[0] - var2[0]) + abs(var1[1] - var2[1]) == 1

    def _is_friend(self, val1, val2):
        return val2 in self.friends[val1]

    def get_neighbours(self, var):
        res = []
        i, j = var
        for k in range(4):
            ni, nj = i+self.dict[k][0], j+self.dict[k][1]
            if (0 <= ni and ni < self.n) and (0 <= nj and nj < self.m):
                res.append((ni, nj))
        return res

    def nconflicts(self, var, val, assignment):
        """Return the number of conflicts var=val has with other variables."""

        # Subclasses may implement this more efficiently
        def conflict(var2):
            if var2 in assignment:
                return not self.constraints(
                    var, val, var2, assignment[var2])
            return False

        return count(conflict(v) for v in self.neighbors[var]) + \
            len(assignment.values()) - len(set(assignment.values()))

    def result(self, state, action):
        """Perform an action and return the new state."""
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        """The goal is to assign all variables, with all constraints satisfied."""
        assignment = state
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0 for variables in self.variables))

    def choices(self, var, assignment):
        """Return all values for var that aren't currently ruled out."""
        # return self.getDomain(assignment)
        return (self.curr_domains or self.domains)[var]

    def display(self, assignment):
        seats = np.empty((self.n, self.m), dtype=int)

        for (i, j), val in assignment.items():
            seats[i, j] = val

        print(seats)
