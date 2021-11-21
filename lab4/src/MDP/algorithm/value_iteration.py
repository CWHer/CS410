from icecream import ic
from utils import expected_utility


def value_iteration(mdp, epsilon=0.001):
    """
    Solving an MDP by value iteration. [You may refer to Lecture 6, Slide 55 and Figure 17.4 in the reference book]

    paras: an MDP, an accuracy parameter epsilon which indicates the maximum change in the utility of any state in an iteration

    return: utilities, the optimal policy (to extract the optimal policy, you may use the best_policy() function)
    """
    # results = []
    U = {s: 0 for s in mdp.states}
    # results.append(U)
    while True:
        """ YOUR CODE HERE """
        U_new, delta = dict(), 0
        for s in mdp.states:
            Q_values = [
                expected_utility(a, s, U, mdp)
                for a in mdp.actions(s)]
            U_new[s] = max(Q_values)
            delta = max(delta, U_new[s] - U[s])
        U = U_new
        # results.append(U)
        if delta < epsilon:
            break

    # import pickle
    # with open("VI_2.0.pkl", "wb") as f:
    #     pickle.dump(results, f)

    return U, best_policy(mdp, U)


def best_policy(mdp, U):
    """
    Conduct policy extraction by using the function expected_utility(). Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. [You may refer to Lecture 6, Slide 66]

    paras: an MDP, utilities U

    return: the extracted best policy
    """

    """ YOUR CODE HERE """
    policy = {}
    for s in mdp.states:
        actions = mdp.actions(s)
        Q_values = [
            expected_utility(a, s, U, mdp)
            for a in actions]
        policy[s] = actions[Q_values.index(max(Q_values))]
    return policy
