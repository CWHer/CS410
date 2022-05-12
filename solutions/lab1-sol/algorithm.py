from problem import Direction


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

    class Path(object):
        def __init__(self, locations, directions, cost):
            self.locations = locations
            self.directions = directions
            self.cost = cost

    path = Path([problem.get_start()],[],0)

    if problem.is_goal(problem.get_start()):
        return path.directions

    stack = Stack()
    stack.push(path)

    while not stack.is_empty():
        currentPath = stack.pop()
        currentLocation = currentPath.locations[-1]
        if problem.is_goal(currentLocation):
            return currentPath.directions
        else:
            nextSteps = problem.get_successors(currentLocation)
            for nextStep in nextSteps:
                nextLocation = nextStep[0]
                nextDirection = nextStep[1]
                nextCost = nextStep[2]
                if nextLocation not in currentPath.locations:
                    nextLocations = currentPath.locations[:]
                    nextLocations.append(nextLocation)
                    nextDirections = currentPath.directions[:]
                    nextDirections.append(nextDirection)
                    nextCosts = currentPath.cost + nextCost
                    nextPath = Path(nextLocations, nextDirections, nextCosts)
                    stack.push(nextPath)

    return []

def breadth_first_search(problem):
    """Returns a sequence of moves that solves general maze problems with BFS.

    Search the shallowest nodes in the search tree first.
    """
    from util import Queue

    class Path(object):
        def __init__(self, locations, directions, cost):
            self.locations = locations
            self.directions = directions
            self.cost = cost

    path = Path([problem.get_start()],[],0)

    if problem.is_goal(problem.get_start()):
        return path.directions

    queue = Queue()
    queue.push(path)
    visited = [problem.get_start()]

    while not queue.is_empty():
        currentPath = queue.pop()
        currentLocation = currentPath.locations[-1]
        if problem.is_goal(currentLocation):
            return currentPath.directions
        else:
            nextSteps = problem.get_successors(currentLocation)
            for nextStep in nextSteps:
                nextLocation = nextStep[0]
                nextDirection = nextStep[1]
                nextCost = nextStep[2]
                if (nextLocation not in currentPath.locations) and (nextLocation not in visited):
                    if not problem.is_goal(nextLocation):
                        visited.append(nextLocation)
                    nextLocations = currentPath.locations[:]
                    nextLocations.append(nextLocation)
                    nextDirections = currentPath.directions[:]
                    nextDirections.append(nextDirection)
                    nextCosts = currentPath.cost + nextCost
                    nextPath = Path(nextLocations, nextDirections, nextCosts)
                    queue.push(nextPath)

    return []
