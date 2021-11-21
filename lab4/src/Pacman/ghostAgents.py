# ghostAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import Agent
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util


class GhostAgent(Agent):
    def __init__(self, index):
        self.index = index

    def getAction(self, state):
        dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution(dist)

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined()


class RandomGhost(GhostAgent):
    "A ghost that chooses a legal action uniformly at random."

    def getDistribution(self, state):
        dist = util.Counter()
        for a in state.getLegalActions(self.index):
            dist[a] = 1.0
        dist.normalize()
        return dist


class DirectionalGhost(GhostAgent):
    "A ghost that prefers to rush Pacman, or flee when scared."

    def __init__(self, index, prob_attack=0.8, prob_scaredFlee=0.8):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee

    def getDistribution(self, state):
        # Read variables from state
        ghostState = state.getGhostState(self.index)
        legalActions = state.getLegalActions(self.index)
        pos = state.getGhostPosition(self.index)
        isScared = ghostState.scaredTimer > 0

        speed = 1
        if isScared:
            speed = 0.5

        actionVectors = [Actions.directionToVector(
            a, speed) for a in legalActions]
        newPositions = [(pos[0]+a[0], pos[1]+a[1]) for a in actionVectors]
        pacmanPosition = state.getPacmanPosition()

        # Select best actions given the state
        distancesToPacman = [manhattanDistance(
            pos, pacmanPosition) for pos in newPositions]
        if isScared:
            bestScore = max(distancesToPacman)
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min(distancesToPacman)
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip(
            legalActions, distancesToPacman) if distance == bestScore]

        # Construct distribution
        dist = util.Counter()
        for a in bestActions:
            dist[a] = bestProb / len(bestActions)
        for a in legalActions:
            dist[a] += (1-bestProb) / len(legalActions)
        dist.normalize()
        return dist


def scoreEvaluationFunctionGhost(currentGameState):
    return currentGameState.getScore()


class MinimaxGhost(GhostAgent):
    def __init__(self, index, evalFn='scoreEvaluationFunctionGhost', depth='2'):
        self.index = index  # Ghosts are always with index > 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth, self.index and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        from icecream import ic

        def search(depth, index, state):
            """[summary]

            Args:
                depth (int): [description]
                index (int): [description] k-th agent. 
            """
            if index == state.getNumAgents():
                return search(depth + 1, 0, state)

            if depth == self.depth or \
                    state.isWin() or state.isLose():
                return self.evaluationFunction(state), None

            actions = state.getLegalActions(index)
            scores = []
            for action in actions:
                next_state = state.generateSuccessor(index, action)
                score, _ = search(depth, index + 1, next_state)
                scores.append(score)

            node_fn = max if index == 0 else min
            score = node_fn(scores)
            action_indices = [i for i in range(
                len(scores)) if scores[i] == score]
            action_index = random.choice(action_indices)
            return score, action_index

        ic.disable()
        ic.configureOutput(includeContext=True)
        score, action = search(0, self.index, gameState)
        # ic.enable()
        ic(score, action)
        return gameState.getLegalActions(self.index)[action]
