def no_inference(csp, var, value, assignment, removals):
    return True

def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()  # It is necessary for using csp.prune()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True

def AC3(csp, removals=None):
    def revise(Xi, Xj):
        """Return true if we remove a value."""
        revised = False
        for x in csp.curr_domains[Xi][:]:
            conflict = True
            for y in csp.curr_domains[Xj]:
                if csp.constraints(Xi, x, Xj, y):
                    conflict = False
                if not conflict:
                    break
            if conflict:
                csp.prune(Xi, x, removals)
                revised = True
        return revised

    queue = [(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]]
    csp.support_pruning()  # It is necessary for using csp.prune()
    while queue:
        (Xi, Xj) = queue.pop(0)
        revised = revise(Xi, Xj)
        if revised:
            if not csp.curr_domains[Xi]:
                return False  # CSP is inconsistent
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True  # CSP is satisfiable

def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp, removals)
