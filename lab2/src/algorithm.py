from problem import Direction
import math
from icecream import ic
# from dataclasses import dataclass, field
# from typing import Any, Tuple


class SearchAlgorithm:
    def __init__(self, algo_name):
        assert algo_name in ["tiny", "bfs", "dfs", "Exercise2_1_1", "Exercise2_1_2",
                             "Exercise2_2_1", "Exercise2_2_2", "Exercise2_3_1"], "Invalid algorithm."

        if algo_name == "tiny":
            self._solver = tiny_maze_search
        elif algo_name == "bfs":
            self._solver = breadth_first_search
        elif algo_name == "dfs":
            self._solver = depth_first_search

        # for Lab 2
        elif algo_name == "Exercise2_1_1":
            self._solver = Exercise2_1_1
        elif algo_name == "Exercise2_1_2":
            self._solver = Exercise2_1_2
        elif algo_name == "Exercise2_2_1":
            self._solver = Exercise2_2_1
        elif algo_name == "Exercise2_2_2":
            self._solver = Exercise2_2_2
        elif algo_name == "Exercise2_3_1":
            self._solver = Exercise2_3_1

    def __call__(self, problem):
        return self._solver(problem)


def tiny_maze_search(problem):
    """Returns a sequence of moves that solves tinyMaze."""
    s = Direction.SOUTH
    w = Direction.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
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

    return []


def breadth_first_search(problem):
    """Returns a sequence of moves that solves general maze problems with BFS.

    Search the shallowest nodes in the search tree first.
    """
    from util import Queue

    """ YOUR CODE HERE """

    return []

# ****************************** For Lab 2 ******************************


def Exercise2_1_1(problem):
    """
    Returns the number of lakes using depth-first graph search (DFGS).

    Please note that some APIs in the environment of Lab 2 are slightly different from them in the environment of Lab 1.
    """
    from util import Stack
    """ YOUR CODE HERE """

    lakes_cnt = 0
    visited, stack = set(), Stack()
    layout = problem._layout
    for i in range(layout._width):
        for j in range(layout._height):
            if (not (i, j) in visited and
                    layout.is_wall((i, j))):
                # DFGS
                lakes_cnt += 1
                stack.push((i, j))
                while not stack.is_empty():
                    cur_state = stack.pop()
                    visited.add(cur_state)
                    for state, *_ in problem.get_successors(
                            cur_state, wall=1):
                        if not state in visited:
                            visited.add(state)
                            stack.push(state)

    return lakes_cnt


def Exercise2_1_2(problem):
    """
    Returns the path from S to G using DFGS with the iterative deepening trick.
    """
    from util import Stack
    """ YOUR CODE HERE """
    # ic.disable()
    # ic.enable()

    def DFGS(depth, problem):
        # DFGS
        time_log, memory_log = 0, 0
        visited, stack = set(), Stack()
        stack.push((0, problem.get_start()))
        while not stack.is_empty():
            time_log += 1
            memory_log = max(memory_log, len(stack._list))

            cur_dep, cur_state = stack.pop()
            if problem.is_goal(cur_state):
                # ic(time_log, memory_log)
                return cur_dep
            for state, *_ in problem.get_successors(
                    cur_state):
                if (cur_dep < depth and
                        not state in visited):
                    visited.add(state)
                    stack.push((cur_dep + 1, state))
        # ic(time_log, memory_log)
        return None

    max_dep = (problem._layout._width *
               problem._layout._height)

    # NOTE: increasing function 1
    #   step = 1
    for depth in range(1, max_dep, 1):
        find_goal = DFGS(depth, problem)
        if not find_goal is None:
            return f"find Goal with depth {depth}"

    # NOTE: increasing function 2
    #   step = 5
    # for depth in range(0, max_dep, 5):
    #     find_goal = DFGS(depth, problem)
    #     if not find_goal is None:
    #         return f"find Goal with depth {depth}"
    # DO NOT find goal
    return "fail to find Goal"


def Exercise2_2_1(problem):
    """
    Returns the least-cost path from S to G and its cost using uniform-cost graph search (UCGS)
    """
    from queue import PriorityQueue
    """ YOUR CODE HERE """
    def UCGS(problem):
        class Node():
            """[summary]
            naive link list to store actions
            """

            def __init__(self,
                         state, cost,
                         direction=None,
                         pre_node=None) -> None:
                self.cost = cost
                self.state = state
                self.direction = direction
                self.pre_node = pre_node

            def __lt__(self, rhs):
                return self.cost < rhs.cost

            def getSol(self):
                if self.pre_node is None:
                    return []
                return self.pre_node.getSol() + [self.direction]

        # ic.disable()
        # ic.enable()
        # NOTE: state = (pos, dir, cost)
        queue, frontier, explored = PriorityQueue(), dict(), set()
        queue.put(Node(problem.get_start(), 0, 0))
        while not queue.empty():
            cur_node = queue.get()
            if cur_node.state in explored:
                continue
            explored.add(cur_node.state)

            if problem.is_goal(cur_node.state):
                ic(len(explored))
                return cur_node.getSol()

            for state, direction, cost in problem.get_successors(cur_node.state):
                cost = cur_node.cost + cost
                # ic(state, direction, cost)
                if (not state in explored
                    and (not state in frontier
                         or frontier[state] > cost)):
                    frontier[state] = cost
                    queue.put(Node(state,
                                   cur_node.cost + cost,
                                   direction, cur_node))
        return None

    # ic.enable()
    result = UCGS(problem)
    print(result)
    if not result is None:
        return problem.eval_actions(result)
    return None


def Heuristic1(state1, state2):  # the first heuristic function using Euclidean distance
    """ YOUR CODE HERE """
    x1, y1 = state1
    x2, y2 = state2
    return math.sqrt((x1 - x2) * (x1 - x2)
                     + (y1 - y2) * (y1 - y2))


def Exercise2_2_2(problem):
    """
    Returns the path from S to G using greedy graph search (GGS).
    """
    from queue import PriorityQueue
    """ YOUR CODE HERE """
    def GGS(problem):
        class Node():
            """[summary]
            naive link list to store actions
            """

            def __init__(self,
                         state, h, cost,
                         direction=None,
                         pre_node=None) -> None:
                self.h = h
                self.cost = cost
                self.state = state
                self.direction = direction
                self.pre_node = pre_node

            def __lt__(self, rhs):
                return (self.h < rhs.h
                        if math.fabs(self.h - rhs.h) > 1e-5
                        else self.cost > rhs.cost)

            def getSol(self):
                if self.pre_node is None:
                    return []
                return self.pre_node.getSol() + [self.direction]

        # ic.disable()
        # ic.enable()
        # NOTE: state = (pos, dir, cost)
        queue, frontier, explored = PriorityQueue(), dict(), set()
        queue.put(Node(problem.get_start(), 0, 0))
        while not queue.empty():
            cur_node = queue.get()
            if cur_node.state in explored:
                continue
            explored.add(cur_node.state)

            if problem.is_goal(cur_node.state):
                ic(len(explored))
                return cur_node.getSol()

            for state, direction, cost in problem.get_successors(cur_node.state):
                h = Heuristic1(problem.get_goal(), state)
                # ic(state, direction, cost)
                if (not state in explored
                    and (not state in frontier
                         or frontier[state] > h)):
                    frontier[state] = h
                    queue.put(Node(state, h,
                                   cur_node.cost + cost,
                                   direction, cur_node))
        return None

    result = GGS(problem)
    print(result)
    if not result is None:
        return problem.eval_actions(result)
    return None


def Heuristic2(state1, state2):  # the second heuristic function
    """ YOUR CODE HERE """
    x1, y1 = state1
    x2, y2 = state2
    return math.fabs(x1 - x2) + math.fabs(y1 - y2)


def Exercise2_3_1(problem):
    """
    Returns the least-cost path from S to G and its cost using a-star graph search (ASGS)
    """
    from queue import PriorityQueue
    """ YOUR CODE HERE """
    def AStarGS(problem):
        class Node():
            """[summary]
            naive link list to store actions
            """

            def __init__(self,
                         state, f, cost,
                         direction=None,
                         pre_node=None) -> None:
                self.f = f
                self.cost = cost
                self.state = state
                self.direction = direction
                self.pre_node = pre_node

            def __lt__(self, rhs):
                return (self.f < rhs.f
                        if math.fabs(self.f - rhs.f) > 1e-5
                        else self.cost > rhs.cost)

            def getSol(self):
                if self.pre_node is None:
                    return []
                return self.pre_node.getSol() + [self.direction]

        # ic.disable()
        # NOTE: state = (pos, dir, cost)
        queue, frontier, explored = PriorityQueue(), dict(), set()
        queue.put(Node(problem.get_start(), 0, 0))
        while not queue.empty():
            cur_node = queue.get()
            # ic(cur_node.f)
            if cur_node.state in explored:
                continue
            explored.add(cur_node.state)

            if problem.is_goal(cur_node.state):
                ic(len(explored))
                return cur_node.getSol()

            for state, direction, cost in problem.get_successors(cur_node.state):
                f = cur_node.cost + cost + \
                    Heuristic1(problem.get_goal(), state)
                # f = cur_node.cost + cost + \
                #     Heuristic2(problem.get_goal(), state)
                # ic(state, direction, cost)
                if (not state in explored
                    and (not state in frontier
                         or frontier[state] > f)):
                    frontier[state] = f
                    queue.put(Node(state, f,
                                   cur_node.cost + cost,
                                   direction, cur_node))
        return None

    result = AStarGS(problem)
    print(result)
    if not result is None:
        return problem.eval_actions(result)
    return None
