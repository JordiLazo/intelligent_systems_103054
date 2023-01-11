# multiAgents.py
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        pacmanPosition = currentGameState.getPacmanPosition()
        currentFood = currentGameState.getFood().asList()
        totalScore = 0
        for x,y in currentFood:
            d = manhattanDistance((x,y),newPos)
            totalScore += 2000 if d == 0 else 1 / (d ** 2)

        for ghost in newGhostStates:
            d = manhattanDistance(ghost.getPosition(),newPos)
            if d > 1:
                continue
            totalScore += 3000 if ghost.scaredTimer !=0 else -3000
        return totalScore


        #return childGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def terminal_test(self,state,depth):
        return depth == 0 or state.isWin() or state.isLose()

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        v = float("-inf")
        actions = []
        for a in gameState.getLegalActions(agentIndex=0):
            successor = gameState.getNextState(agentIndex=0,action=a)
            undefined = self.min_value(successor,agent = 1,depth= self.depth)
            if undefined == v:
                actions.append(a)
            elif undefined > v:
                v = undefined
                actions = [a]
        
        return actions[0]

    def min_value(self, gameState,agent,depth):
        if self.terminal_test(gameState,depth):
            return self.evaluationFunction(gameState)

        v = float("inf")
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent,action=a)
            if agent == gameState.getNumAgents() - 1:
                v= min(v,self.max_value(successor,agent=0,depth = depth -1 ))
            else:
                v = min(v,self.min_value(successor,agent=agent+1,depth=depth))
        return v

    def max_value(self,gameState,agent,depth):
        if self.terminal_test(gameState,depth):
            return self.evaluationFunction(gameState)

        v = float("-inf")
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent,action=a)
            v = max(v,self.min_value(successor,agent=1,depth=depth))
        return v

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    best_action = None
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        beta = float("inf")
        alpha = float("-inf")
        self.max_value(gameState,agent=0,depth=self.depth,alpha=alpha,beta=beta)
        return self.best_action

    def max_value(self,gameState,agent,depth,alpha,beta):
        if self.terminal_test(gameState,depth):
            return self.evaluationFunction(gameState)

        v = float("-inf")
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent,action=a)
            v = max(v,self.min_value(successor,agent=1,depth=depth,alpha=alpha,beta=beta))
            if v > beta:
                return v
            if v > alpha:
                alpha = v
                # update best action
                self.best_action = a  # current level best action
        return v
    
    def min_value(self,gameState,agent,depth,alpha,beta):
        if self.terminal_test(gameState,depth):
            return self.evaluationFunction(gameState)
        v = float("inf")
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent,action=a)
            if agent == gameState.getNumAgents() -1 :
                v = min(v,self.max_value(successor,agent=0,depth=depth-1,alpha=alpha,beta=beta))
            else:
                v = min(v,self.min_value(successor,agent=agent+1,depth=depth,alpha=alpha,beta=beta))
            if v < alpha:
                return v
            beta = min(beta,v)
        return v

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        v = float("-inf")
        actions = []
        for a in gameState.getLegalActions(agentIndex=0):
            successor = gameState.getNextState(agentIndex=0,action=a)
            undefined = self.exp_value(successor,agent = 1,depth= self.depth)
            if undefined == v:
                actions.append(a)
            elif undefined > v:
                v = undefined
                actions = [a]
        
        return actions[0]
    def max_value(self, gameState, agent, depth):
        if self.terminal_test(gameState, depth):
            return self.evaluationFunction(gameState)

        v = float("-inf")
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent, action=a)
            v = max(v, self.exp_value(successor, agent=1, depth=depth))
        return v

    def exp_value(self, gameState, agent, depth):
        if self.terminal_test(gameState, depth):
            return self.evaluationFunction(gameState)

        v = 0
        legal_actions = len(gameState.getLegalActions(agent))
        for a in gameState.getLegalActions(agent):
            successor = gameState.getNextState(agent, action=a)
            if agent == gameState.getNumAgents() - 1:
                v += 1/legal_actions* self.max_value(successor,0,depth-1)
            else:
                v += 1/legal_actions* self.exp_value(successor,agent+1,depth)
        return v


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacmanPosition = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    foodPosition = food.asList()
    foodPosition = sorted(foodPosition,key = lambda position: manhattanDistance(pacmanPosition,position))
    closestFoodDistance = -1
    if len(foodPosition) > 0:
        closestFoodDistance = manhattanDistance(foodPosition[0], pacmanPosition)

    distanceToGhost = 1
    proximityToGhost = 0
    for ghostState in currentGameState.getGhostStates():
        distance = manhattanDistance(pacmanPosition, ghostState.getPosition())
        distanceToGhost += distance

        if distance <= 1:
            proximityToGhost += 1

    newCapsules = currentGameState.getCapsules()
    numberOfCapsules = len(newCapsules)
    return currentGameState.getScore() + (1/float(closestFoodDistance)) - (1/float(distanceToGhost)) - proximityToGhost - numberOfCapsules


    # util.raiseNotDefined()    

# Abbreviation
better = betterEvaluationFunction
