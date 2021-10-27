import queue
from icecream import ic
import copy


class Variable():
    def __init__(self, domain, name="var") -> None:
        self.name = name
        self.domain = domain
        self.val = None

    def getVal(self):
        return self.val

    def emptyDomain(self):
        return not self.domain

    def nextVal(self):
        for val in self.domain:
            self.val = val
            yield
        # raise StopIteration()

    def __str__(self) -> str:
        return "{}: {}".format(self.name,
                               [self.domain] if self.val is None else [self.val])


class ReduceDomain():
    def __init__(self, k,  domains, func) -> None:
        self.k = k
        # domain of variable[k]
        self.k_domain = domains[k]
        # domain of other variables
        self.res_domains = domains[:k] + domains[k + 1:]
        self.test_func = func
        self.value = [0 for _ in range(len(domains) - 1)]

    def search(self, k, val):
        """[summary]
        search all
            domain[0] x domain[1] x ...
        and return all possible value of variable[x]
        """
        if k == len(self.res_domains):
            values = (self.value[:self.k]
                      + [val] + self.value[self.k:])
            # ic(values)
            return self.test_func(values)
        for self.value[k] in self.res_domains[k]:
            if self.search(k + 1, val):
                return True
        return False

    # API
    def reduce(self):
        domain = []
        for val in self.k_domain:
            if self.search(0, val):
                domain.append(val)
        return domain


class Constraint():
    def __init__(self) -> None:
        self.variables = []
        self.test_func = None

    def addVar(self, var: Variable):
        self.variables.append(var)

    def addVars(self, vars):
        self.variables.extend(vars)

    def setTest(self, func):
        self.test_func = func

    def runTest(self):
        return self.test_func([var.getVal() for var in self.variables])

    def reduceDomain(self, k):
        """[summary]
        get reduced domain of variables[k]
        """
        # domain[0] x domain[1] x ...
        domains = [(var.domain
                    if var.val is None else [var.val])
                   for var in self.variables]
        solver = ReduceDomain(k, domains, self.test_func)
        return solver.reduce()


class Problem():
    def __init__(self) -> None:
        """[summary]
        NOTE: add variables before constraints !!
        """
        self.variables = []
        self.constraints = []
        # NOTE: for forward checking
        #   constraints related to a variable
        self.var_cons = dict()

    # APIs
    def addVar(self, var: Variable):
        self.variables.append(var)
        self.var_cons[var] = []

    def addVars(self, vars):
        for var in vars:
            self.addVar(var)

    def addCons(self, cons: Constraint):
        self.constraints.append(cons)
        for var in cons.variables:
            self.var_cons[var].append(cons)

    def addConss(self, conss):
        for cons in conss:
            self.addCons(cons)

    def getDomain(self):
        return [var.domain for var in self.variables]

    def setDomain(self, domains):
        for i, var in enumerate(self.variables):
            if var.val is None:
                var.domain = domains[i]

    def printState(self):
        for var in self.variables:
            print(var)
        print("")

    def AC3(self, cur_var):
        """[summary]
        NOTE: only works for binary constraint
        """
        # class Arc():
        #     def __init__(self, cons, fix_var) -> None:
        #         self.cons = cons
        #         self.fix_var = fix_var
        #         for var in cons.variables:
        #             if var != fix_var:
        #                 self.nxt_var = var
        #         self.name = "{} --> {}".format(
        #             self.nxt_var.name, self.fix_var.name)

        #     def __str__(self) -> str:
        #         return self.name

        #     def __lt__(self, rhs):
        #         return self.name < rhs.name

        def printArc(cons, fix_var, header="push"):
            for var in cons.variables:
                if var != fix_var:
                    print("{} {} --> {}".format(header, var.name, fix_var.name))

        # from queue import PriorityQueue
        from queue import Queue
        Q = Queue()
        for cons in self.var_cons[cur_var]:
            # display
            printArc(cons, cur_var)
            Q.put((cons, cur_var))
        while not Q.empty():
            cons, fix_var = Q.get()
            printArc(cons, fix_var, "pop")
            for i, var in enumerate(cons.variables):
                if var != fix_var and var.val is None:
                    new_domain = cons.reduceDomain(i)
                    if new_domain < var.domain:
                        print("{}: original domain {}, cross off result {}".format(
                            var.name, var.domain, new_domain))
                        var.domain = new_domain
                        # ic(var.name, var.domain)
                        for cons in self.var_cons[var]:
                            printArc(cons, var)
                            Q.put((cons, var))

    def search(self, k=0):
        if k == len(self.variables):
            for cons in self.constraints:
                if not cons.runTest():
                    return False
            print("find solution!")
            return True

        for var in self.variables:
            if var.emptyDomain():
                print("empty domain detected!\n")
                return False

        for _ in self.variables[k].nextVal():
            print("Current Variable {}".format(self.variables[k]))
            domains = copy.deepcopy(self.getDomain())

            # NOTE: forward checking

            # CASE 1: check and cross one by one
            # for cons in self.var_cons[self.variables[k]]:
            #     for i, var in enumerate(cons.variables):
            #         if var.getVal() is None:
            #             var.domain = cons.reduceDomain(i)
            #             # ic(var.name, var.domain)

            # CASE 2: check all, then cross
            new_domains = dict()
            for var in self.variables:
                new_domains[var] = set(var.domain)
            for cons in self.var_cons[self.variables[k]]:
                for i, var in enumerate(cons.variables):
                    if var.getVal() is None:
                        new_domains[var] &= set(cons.reduceDomain(i))
            for var in self.variables:
                var.domain = sorted(list(new_domains[var]))

            self.printState()

            # NOTE: AC3
            # print("AC3 start")
            # self.AC3(self.variables[k])
            # print("AC3 end")
            # self.printState()

            if self.search(k + 1):
                return True
            self.setDomain(domains)

        self.variables[k].val = None
        return False


# simple test
# var1 = Variable([1, 2, 3], "x1")
# var2 = Variable([2, 9, 10], "x2")

# cons = Constraint()
# cons.addVar(var1)
# cons.addVar(var2)
# cons.setTest(lambda x: sum(x) == 4)

# problem = Problem()
# problem.addVar(var1)
# problem.addVar(var2)
# problem.addCons(cons)

# ic(problem.search())
# for var in problem.variables:
#     print(var)

# Ex 3
X3 = Variable([0, 1], "X3")
F = Variable(list(range(1, 10)), "F")
X2 = Variable([0, 1], "X2")
X1 = Variable([0, 1], "X1")
O = Variable(list(range(10)), "O")
T = Variable(list(range(10)), "T")
R = Variable(list(range(10)), "R")
U = Variable(list(range(10)), "U")
W = Variable(list(range(10)), "W")

cons1 = Constraint()
cons1.addVars([O, R, X1])
cons1.setTest(lambda w: w[0] + w[0] == w[2] * 10 + w[1])

cons2 = Constraint()
cons2.addVars([W, U, X1, X2])
cons2.setTest(lambda w: w[0] + w[0] + w[2] == w[3] * 10 + w[1])

cons3 = Constraint()
cons3.addVars([T, O, X2, X3])
cons3.setTest(lambda w: w[0] + w[0] + w[2] == w[3] * 10 + w[1])

cons4 = Constraint()
cons4.addVars([F, X3])
cons4.setTest(lambda w: w[0] == w[1])

cons5 = Constraint()
cons5.addVars([F, T, U, W, R, O])
cons5.setTest(lambda w: len(w) == len(set(w)))

problem = Problem()
problem.addVars([X3, F, X2, X1, O, T, R, U, W])
problem.addConss([cons1, cons2, cons3, cons4, cons5])
ic(problem.search())
problem.printState()

# Ex 4
# A = Variable([3, 2, 1], "A")
# B = Variable([3, 2, 1], "B")
# C = Variable([3, 2, 1], "C")
# D = Variable([3, 2, 1], "D")

# cons1 = Constraint()
# cons1.addVars([A, B])
# cons1.setTest(lambda w: w[0] != w[1])

# cons2 = Constraint()
# cons2.addVars([B, C])
# cons2.setTest(lambda w: w[0] > w[1])

# cons3 = Constraint()
# cons3.addVars([C, D])
# cons3.setTest(lambda w: w[0] < w[1])

# problem = Problem()
# problem.addVars([A, B, C, D])
# problem.addConss([cons1, cons2, cons3])
# ic(problem.search())
# problem.printState()
