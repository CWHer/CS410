def no_inference(csp, var, value, assignment, removals):
    return True


def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    csp.support_pruning()  # It is necessary for using csp.prune()
    """ YOUR CODE HERE """
    for X in csp.neighbors[var]:
        for x in csp.curr_domains[X]:
            if not csp.constraints(X, x, var, value):
                csp.prune(X, x, removals)

    return True


def AC3(csp, var, removals=None):
    def revise(Xi, Xj):
        """Return true if we remove a value."""
        """ YOUR CODE HERE """
        remove = False
        for x in csp.curr_domains[Xi]:
            # print(Xj, csp.curr_domains[Xj])
            satisfied = any(map(
                lambda y: csp.constraints(Xi, x, Xj, y),
                csp.curr_domains[Xj]))
            if not satisfied:
                remove = True
                csp.prune(Xi, x, removals)
        return remove

    csp.support_pruning()  # It is necessary for using csp.prune()

    # from icecream import ic
    from queue import Queue
    queue = Queue()

    for X in csp.neighbors[var]:
        queue.put((X, var))
    # print(queue.qsize())
    while not queue.empty():
        """ YOUR CODE HERE """
        Xi, Xj = queue.get()
        if revise(Xi, Xj):
            for Xk in csp.neighbors[Xi]:
                queue.put((Xk, Xi))
    # ic("AC3 finish")
    return True  # CSP is satisfiable


def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Maintain arc consistency."""
    return constraint_propagation(csp, var, removals)
