from icecream import ic
from utils  import expected_utility

def value_iteration(mdp, epsilon=0.001):
    """
    Solving an MDP by value iteration. [You may refer to Lecture 6, Slide 55 and Figure 17.4 in the reference book]
    
    paras: an MDP, an accuracy parameter epsilon which indicates the maximum change in the utility of any state in an iteration

    return: utilities, policy
    """

    U1 = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = max([expected_utility(a, s, U, mdp) for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta <= epsilon * (1 - gamma) / gamma:
            return U, best_policy(mdp, U)

def best_policy(mdp, U):
    """
    Conduct policy extraction. Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. [You may refer to Lecture 6, Slide 66]
    
    paras: an MDP, utilities U

    return: the extracted best policy
    """
    pi = {}
    for s in mdp.states:
        pi[s] = max(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
    return pi