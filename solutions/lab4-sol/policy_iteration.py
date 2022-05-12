import random

from utils  import expected_utility

def policy_iteration(mdp):
    """
    Solve an MDP by policy iteration [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]
    
    paras: an MDP

    return: utilities, policy
    """
    U = {s: 0 for s in mdp.states}
    pi = {s: random.choice(mdp.actions(s)) for s in mdp.states}
    while True:
        U = policy_evaluation(pi, mdp)
        unchanged, pi = policy_improvement(pi, U, mdp)
        if unchanged:
            return U, pi

def policy_evaluation(pi, mdp, iteration_num=50):
    """
    Return an updated utility mapping U from each state in the MDP to its
    utility [You may refer to idea 1 in Lecture 6, Slide 75 and Figure 17.7 in the reference book]
    
    paras: current policy pi, mdp

    return: utilities, policy
    """
    U = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(iteration_num):
        for s in mdp.states:
            U[s] = expected_utility(pi[s], s, U, mdp)
    return U

def policy_improvement(pi, U, mdp):
    """
    Conduct policy improvement [You may refer to Lecture 6, Slide 72 and Figure 17.7 in the reference book]
    
    paras: current policy pi, current utilities U, the MDP mdp

    return: a bool variable which indicates whether the policy improvement is convergent, an improved policy of policy pi
    """
    unchanged = True
    for s in mdp.states:
        a = max(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
        if a != pi[s]:
            pi[s] = a
            unchanged = False
    return unchanged, pi

