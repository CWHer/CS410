from problem import Direction, SearchProblem


class SearchAlgorithm:
    def __init__(self, algo_name):
        assert algo_name in ["tiny", "bfs", "dfs"], "Invalid algorithm."

        if algo_name == "tiny":
            self._solver = tiny_maze_search
        elif algo_name == "bfs":
            self._solver = breadth_first_search
        elif algo_name == "dfs":
            self._solver = depth_first_search

    def __call__(self, problem):
        return self._solver(problem)


def tiny_maze_search(problem):
    """Returns a sequence of moves that solves tinyMaze."""
    s = Direction.SOUTH
    w = Direction.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem: SearchProblem):
    """Returns a sequence of moves that solves general maze problems with DFS.

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. To get started, you might leverage your Stack structure and the APIs
    provided in the Problem class:

    print("Start:", problem.get_start())
    print("Is the start a goal?", problem.is_goal(problem.get_start()))
    print("Start's successors:", problem.get_successors(problem.get_start()))
    """
    from util import Stack

    """ YOUR CODE HERE """
    # print("Start:", problem.get_start())
    # print("Is the start a goal?", problem.is_goal(problem.get_start()))
    # print("Start's successors:", problem.get_successors(problem.get_start()))

    class Node():
        """[summary]
        naive link list to store actions
        """

        def __init__(self, state,
                     pre_node=None) -> None:
            self.state = state
            self.pre_node = pre_node

        def getSol(self):
            if self.pre_node is None:
                return []
            sol = self.pre_node.getSol()
            sol.append(self.state[1])
            return sol

    # NOTE: state = (pos, dir, cost)
    stack, visited = Stack(), set()
    stack.push(Node([problem.get_start()]))
    while not stack.is_empty():
        cur_node = stack.pop()
        if problem.is_goal(cur_node.state[0]):
            return cur_node.getSol()
        for state in problem.get_successors(
                cur_node.state[0]):
            if not state[0] in visited:
                visited.add(state[0])
                stack.push(Node(state, cur_node))
    return []


def breadth_first_search(problem: SearchProblem):
    """Returns a sequence of moves that solves general maze problems with BFS.

    Search the shallowest nodes in the search tree first.
    """
    from util import Queue

    """ YOUR CODE HERE """
    class Node():
        """[summary]
        naive link list to store actions
        """

        def __init__(self, state,
                     pre_node=None) -> None:
            self.state = state
            self.pre_node = pre_node

        def getSol(self):
            if self.pre_node is None:
                return []
            sol = self.pre_node.getSol()
            sol.append(self.state[1])
            return sol

    # NOTE: state = (pos, dir, cost)
    queue = Queue()
    queue.push(Node([problem.get_start()]))
    while not queue.is_empty():
        cur_node = queue.pop()
        if problem.is_goal(cur_node.state[0]):
            return cur_node.getSol()
        for state in problem.get_successors(
                cur_node.state[0]):
            queue.push(Node(state, cur_node))
    return []
