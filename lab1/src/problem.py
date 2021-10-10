from enum import Enum


class Direction(Enum):
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"


class Actions:
    _directions = {
        Direction.NORTH: (0, 1),
        Direction.SOUTH: (0, -1),
        Direction.EAST: (1, 0),
        Direction.WEST: (-1, 0),
    }

    @staticmethod
    def direction_to_vector(direction):
        dx, dy = Actions._directions[direction]
        return dx, dy


class SearchProblem:
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.

    The state space consists of (x,y) positions in a pacman game.

    Note: this search problem is fully specified; you should NOT change it.
    """
    _illegal_cost = 999999

    def __init__(
        self,
        layout,
        cost_fn=lambda x: 1,
    ):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self._layout = layout
        self._cost_fn = cost_fn

    def get_start(self):
        return self._layout.start

    def is_goal(self, state):
        return state == self._layout.goal

    def get_successors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """

        successors = []
        for action in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
            x, y = state
            dx, dy = Actions.direction_to_vector(action)
            next_x, next_y = int(x + dx), int(y + dy)
            if not self._layout.is_wall((next_x, next_y)):
                next_state = (next_x, next_y)
                cost = self._cost_fn(next_state)
                successors.append((next_state, action, cost))

        return successors

    def eval_actions(self, actions):
        if actions == None:
            return {"cost": self._illegal_cost, "success": False}

        x, y = self.get_start()
        cost = 0
        for action in actions:
            dx, dy = Actions.direction_to_vector(action)
            x, y = int(x + dx), int(y + dy)
            if self._layout.is_wall((x, y)):
                return {"cost": self._illegal_cost, "success": False}
            cost += self._cost_fn((x, y))

        return {"cost": cost, "success": self.is_goal((x, y))}
