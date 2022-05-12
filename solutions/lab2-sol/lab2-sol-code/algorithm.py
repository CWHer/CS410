from problem import Direction
import math


class SearchAlgorithm:
    def __init__(self, algo_name):
        assert algo_name in ["tiny", "bfs", "dfs", "Exercise2_1_1", "Exercise2_1_2", "Exercise2_2_1", "Exercise2_2_2", "Exercise2_3"], "Invalid algorithm."

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
        elif algo_name == "Exercise2_3":
            self._solver = Exercise2_3

    def __call__(self, problem):
        return self._solver(problem)


def tiny_maze_search(problem):
    """Returns a sequence of moves that solves tinyMaze."""
    s = Direction.SOUTH
    w = Direction.WEST
    return  [s, s, w, s, w, w, s, w]

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
    # """
    # Returns the number of lakes using depth-first graph search (DFGS).
    # """
    # from util import Stack
    # """ YOUR CODE HERE """
    # return []

    from util import Stack
    visited = []
    def dfs(state):
        stack = Stack()
        stack.push(state)
        while not stack.is_empty():
            cur_state = stack.pop()
            visited.append(cur_state)
            successors = problem.get_successors(cur_state, 1)
            for nac_tuple in successors:
                nxt_state = nac_tuple[0]
                if nxt_state not in visited:
                    stack.push(nxt_state)

    hei, wid = problem._layout._height, problem._layout._width
    res = 0
    for x in range(wid):
        for y in range(hei):
            if problem._layout.is_wall((x, y)) and (x,y) not in visited:
                res += 1
                dfs((x, y))

    return res

def Exercise2_1_2(problem):
    # """
    # Returns the path from S to G using DFGS with the iterative deepening trick.
    # """
    # from util import Stack
    # """ YOUR CODE HERE """
    # return []

    def depthLimit(t):
        return t 

    def depth_first_search_with_depth_limit(problem, dlimit):
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

        class Path(object):
            def __init__(self, locations, directions, cost, depth):
                self.locations = locations
                self.directions = directions
                self.cost = cost

                self.depth = depth

        path = Path([problem.get_start()],[],0, 0)

        if problem.is_goal(problem.get_start()):
            return path.directions

        stack = Stack()
        stack.push(path)

        while not stack.is_empty():
            currentPath = stack.pop()
            currentLocation = currentPath.locations[-1]
            currentDepth = currentPath.depth

            if currentDepth > dlimit:
                continue

            if problem.is_goal(currentLocation):
                return currentPath.directions
            else:
                nextSteps = problem.get_successors(currentLocation)
                for nextStep in nextSteps:
                    nextLocation = nextStep[0]
                    nextDirection = nextStep[1]
                    nextCost = nextStep[2]
                    nextDepth = currentDepth + 1

                    if nextDepth > dlimit:
                        continue

                    if nextLocation not in currentPath.locations:
                        nextLocations = currentPath.locations[:]
                        nextLocations.append(nextLocation)
                        nextDirections = currentPath.directions[:]
                        nextDirections.append(nextDirection)
                        nextCosts = currentPath.cost + nextCost
                        nextPath = Path(nextLocations, nextDirections, nextCosts, nextDepth)
                        stack.push(nextPath)

        return []
    
    res, t = [], 1
    res = depth_first_search_with_depth_limit(problem, depthLimit(t))
    while res == []:
        t += 1
        res = depth_first_search_with_depth_limit(problem, depthLimit(t))
    return res, t


def Exercise2_2_1(problem):
    # """
    # Returns the least-cost path from S to G and its cost using uniform-cost graph search (UCGS)
    # """
    # """ YOUR CODE HERE """
    # return []

    import queue

    class Node(): # represent one node in the priority queue
        def __init__(self, state, path_cost):
            '''
            state: the state of one node

            path_cost: the current estimation of the cost of the least-cost path from the start state to this state
            '''
            super().__init__()
            self.state, self.path_cost = state, path_cost

        def __lt__(self, Other_node): # reload the < operator with path_cost as the key-word
            return self.path_cost < Other_node.path_cost

    explored_set = set()
    frontier = queue.PriorityQueue()
    frontier.put(Node(problem.get_start(), 0))
    flag = 0 # whether find the path successfully
    dis = dict() # record the current estimation of the cost of the least-cost path from the start state to one state
    dis[problem.get_start()] = 0
    pre_state = dict() # record the father node of one node on the least-cost path
    goal_state = ''
    while not frontier.empty():
        cur_node = frontier.get()
        cur_state, cur_path_cost = cur_node.state, cur_node.path_cost
        if cur_path_cost > dis[cur_state]:
            continue
        if problem.is_goal(cur_state):
            flag = 1
            goal_state = cur_state
            break
        explored_set.add(cur_state)
        successors = problem.get_successors(cur_state, 0)
        for nac_tuple in successors:
            next_state, action, cost = nac_tuple
            if (next_state not in dis and next_state not in explored_set) or (next_state in dis and dis[next_state] > dis[cur_state] + cost):
                dis[next_state] = dis[cur_state] + cost
                pre_state[next_state] = (cur_state, action)
                frontier.put(Node(next_state, dis[next_state]))
    
    if not flag:
        print('Fail to find the path from S to G!')
        return -1, -1
    else:
        path = []
        cost = dis[goal_state]
        cur_state = goal_state
        while cur_state != problem.get_start():
            path.append(pre_state[cur_state][1])
            cur_state = pre_state[cur_state][0]
        return path[::-1], cost

def Euclidean_dis(state1, state2):
    return math.sqrt((state1[0]-state2[0])**2 + (state1[1]-state2[1])**2)

def Heuristic1(state1, state2): # the first heuristic function using Euclidean distance
    """ YOUR CODE HERE """
    return Euclidean_dis(state1, state2)

def Exercise2_2_2(problem):
    # """
    # Returns the least-cost path from S to G and its cost using greedy graph search (GGS)
    # """
    # """ YOUR CODE HERE """
    # return []

    import queue
    class Node(): # represent one node in the priority queue
        def __init__(self, state, h_function):
            '''
            state: the state of one node

            h_function: heuristic function from this state to the goal state
            '''
            super().__init__()
            self.state, self.h_function = state, h_function

        def __lt__(self, Other_node): # reload the < operator with path_cost as the key-word
            return self.h_function < Other_node.h_function

    start_state, goal_state  = problem.get_start(), problem.get_goal() 
    explored_set = set()
    frontier = queue.PriorityQueue()
    explored_set.add(start_state)
    frontier.put(Node(start_state, Heuristic1(start_state, goal_state)))
    flag = 0 # whether find the path successfully
    pre_state = dict() # record the father node of one node on the least-cost path
    cost = 0
    while not frontier.empty():
        cur_node = frontier.get()
        cur_state, cur_h_function = cur_node.state, cur_node.h_function
        if problem.is_goal(cur_state):
            flag = 1
            break
        successors = problem.get_successors(cur_state, 0)
        for nac_tuple in successors:
            next_state, action, cost = nac_tuple
            if next_state not in explored_set:
                explored_set.add(next_state)
                pre_state[next_state] = (cur_state, action, cost)
                frontier.put(Node(next_state, Heuristic1(next_state, goal_state)))
    
    if not flag:
        print('Fail to find the path from S to G!')
        return -1, -1
    else:
        path = []
        cost = 0
        cur_state = goal_state
        while cur_state != problem.get_start():
            cost += pre_state[cur_state][2]
            path.append(pre_state[cur_state][1])
            cur_state = pre_state[cur_state][0]
        return path[::-1], cost

def Manhattan_dis(state1, state2):
    return abs(state1[0]-state2[0]) + abs(state1[1]-state2[1])

def Heuristic2(state1, state2): # the second heuristic function
    """ YOUR CODE HERE """
    return Manhattan_dis(state1, state2)

def Exercise2_3(problem):
    # """
    # Returns the least-cost path from S to G and its cost using a-star graph search (ASGS)
    # """
    # """ YOUR CODE HERE """
    # return []

    import queue

    class Node(): # represent one node in the priority queue
        def __init__(self, state, weight):
            '''
            state: the state of one node

            weight: the current weight this node
            '''
            super().__init__()
            self.state, self.weight = state, weight

        def __lt__(self, Other_node): # reload the < operator with path_cost as the key-word
            return self.weight < Other_node.weight

    def f_func(g_func, h_func):
        return g_func + h_func

    start_state, goal_state  = problem.get_start(), problem.get_goal()
    explored_set = set()
    flag = 0 # whether find the path successfully
    estimated_f, estimated_g = dict(), dict() # record the current estimation of the f-function, and g-function of one state
    estimated_g[start_state], estimated_f[start_state] =0, f_func(0, Heuristic2(start_state, goal_state))
    frontier = queue.PriorityQueue()
    frontier.put(Node(start_state, estimated_f[start_state]))
    pre_state = dict() # record the father node of one node on the least-cost path
    while not frontier.empty():
        cur_node = frontier.get()
        cur_state, weight = cur_node.state, cur_node.weight
        if weight > estimated_f[cur_state]:
            continue
        if problem.is_goal(cur_state):
            flag = 1
            break
        explored_set.add(cur_state)
        successors = problem.get_successors(cur_state, 0)
        for nac_tuple in successors:
            next_state, action, cost = nac_tuple
            if (next_state not in estimated_f and next_state not in explored_set) or (next_state in estimated_f and estimated_f[next_state] > f_func(estimated_g[cur_state] + cost, Heuristic2(next_state, goal_state))):
                estimated_g[next_state] = estimated_g[cur_state] + cost
                estimated_f[next_state] = f_func(estimated_g[next_state], Heuristic2(next_state, goal_state))
                pre_state[next_state] = (cur_state, action)
                frontier.put(Node(next_state, estimated_f[next_state]))
    
    if not flag:
        print('Fail to find the path from S to G!')
        return -1, -1
    else:
        path = []
        cost = estimated_f[goal_state]
        cur_state = goal_state
        while cur_state != problem.get_start():
            path.append(pre_state[cur_state][1])
            cur_state = pre_state[cur_state][0]
        return path[::-1], cost
