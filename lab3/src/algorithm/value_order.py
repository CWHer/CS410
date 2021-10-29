def unordered_domain_values(var, assignment, csp):
    """The default value order."""
    return csp.choices(var, assignment)


def lcv(var, assignment, csp):
    """Least-constraining-values heuristic."""
    return sorted(csp.choices(var, assignment), key=lambda val: csp.nconflicts(var, val, assignment))
