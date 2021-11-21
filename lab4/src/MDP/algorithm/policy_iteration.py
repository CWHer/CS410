import random

from utils import expected_utility


def policy_iteration(mdp):
    """
    Solve an MDP by policy iteration [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]

    paras: an MDP

    return: utilities, policy
    """
    results = []
    U = {s: 0 for s in mdp.states}
    pi = {s: random.choice(mdp.actions(s)) for s in mdp.states}
    unchanged = False
    results.append(U)
    while not unchanged:
        """ YOUR CODE HERE """
        U = policy_evaluation(pi, mdp)
        unchanged = policy_improvement(pi, U, mdp)
        results.append(U)

    # import pickle
    # with open("PI_2.0.pkl", "wb") as f:
    #     pickle.dump(results, f)

    return U, pi


def policy_evaluation(pi, mdp, iteration_num=50):
    """
    Return an updated utility mapping U from each state in the MDP to its
    utility [You may refer to idea 1 in Lecture 6, Slide 75 and Figure 17.7 in the reference book]

    paras: current policy pi, mdp

    return: utilities
    """
    U = {s: 0 for s in mdp.states}
    for _ in range(iteration_num):
        """ YOUR CODE HERE """
        U_new = dict()
        for s in mdp.states:
            U_new[s] = expected_utility(pi[s], s, U, mdp)
        U = U_new
    return U


def policy_improvement(pi, U, mdp):
    """
    Conduct policy improvement [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]

    paras: current policy pi, current utilities U, the MDP mdp

    return: a bool variable which indicates whether the policy improvement is convergent, an improved policy of policy pi
    """

    """ YOUR CODE HERE """
    unchanged = True
    for s in mdp.states:
        actions = mdp.actions(s)
        Q_values = [
            expected_utility(a, s, U, mdp)
            for a in actions]
        best_action = actions[Q_values.index(max(Q_values))]
        if pi[s] != best_action:
            unchanged = False
            pi[s] = best_action
    return unchanged
