# 103054 - Intelligent Systems

## Summary
1. [Introduction](#introduction)
2. [Learning objectives](#learning-objectives)
3. [Assignment 1](#assignment-1)
4. [Assignment 2](#assignment-2)
5. [Assignment 3](#assignment-3)


## Introduction
In this course, the project will be devoted to the development of a simple videogame. In this subject we will address the artificial intelligence of the project. The graphical part of the game will be addressed in the "Computer graphics and multimedia" subject, while the "Embedded and ubicuos systems" will focus on aspects related to computer-human interaction by means of special devices. Hence, it is strongly recommended to follow through the three subjects at the same time, although it is not mandatory.

The topics of the subject are the following:
- T1. Introduction to Intelligent Systems.
- T2. Advanced Search.
- T3. Reinforcement Learning.
- T4. Supervised machine learning with scikit-learn.
- T5. Unsupervised machine learning with scikit-learn.

## Learning objectives
* Implement and evaluate advanced search algorithms.
* Implement and evaluate reinforcement learning algorithms.
* Apply and evaluate supervised learning algorithms in scikit-learn.
* Apply and evaluate unsupervised learning algorithms in scikit-learn.

## Assignment 1
For the first assignment, you have to work on the "PacMan" project. In particular, you must implement the following algorithms:
- Question 1: Reflex Agent (0 points)
- Question 2: Minimax (2.5 points)
- Question 3: Alpha-Beta Pruning (2.5 points)
- Question 4: Expectimax (2.5 points)
- Question 5: Evaluation Function (2.5 points)
- As an optional task, you can develop the iterative version of the Alpha-Beta algorithm.

The algorithms must be implemented in the file: *multiAgents.py*

In order to check that the answers are good the following command must be executed:
```
python autograder.py
```

The original project can be found in the following link: 
https://inst.eecs.berkeley.edu/~cs188/sp21/project2/

## Assignment 2
On the second assignment we revisit the "PacMan" project, but this time you will work with reinforcement learning.

As with the Adversarial-Search assignment, all the material can be found in: https://inst.eecs.berkeley.edu/~cs188/su21/project3/.

From the project page download the zip file and complete the following tasks, at the end you will have to deliver the whole "PacMan" project including modified, unmodified and added files as a .zip file.

1. Implement the Value Iteration algorithm in valueIterationAgents.py, for this you have to implement the methods computeActionFromValue (state) and computeQValueFromValues(state, action) (2 points)

2. Bridge Crossing Analysis (0.5 point).
    * The agent starts near the low-reward state. With the default discount of 0.9 and the default noise of 0.2, the optimal policy does not corss the bridge.

    <img src="./images/value-q2.png" width="500" height="300" alt="Result of work package 1" title="Result of work package 1" style="display: block; margin: 0 auto"/>

    * Change only ONE of the discount and noise parameters so that the optimal policy causes the agent to cross the bridge. Put your answer in question2() of analysis.py.

3. Find the discount, noise and living reward values that generate the following policies in analysis.py, functions question2a() through question2e(). (1.5 point)

    <img src="./images/discountgrid.png" width="500" height="300" alt="Result of work package 1" title="Result of work package 1" style="display: block; margin: 0 auto"/>
    
   * Prefer the close exit (+1), risking the cliff (-10)
   * Prefer the close exit (+1), but avoiding the cliff (-10)
   * Prefer the distant exit (+10), risking the cliff (-10)
   * Prefer the distant exit (+10), avoiding the cliff (-10)
   * Avoid both exits and the cliff (an episode should never terminate)
   * Your setting of the values should have the property that, if your agent followed its optimal policy in the MDP, it would exhibit the given behaviour. If a particular behaviour cannot be achieved for any setting of parameters return the string 'NOT POSSIBLE'.

4. Q-Learning Agent (2.5 points).
    * Implement the update, computeValueFromQValues, getQValue and computeActionFromQValues methods in qlearningAgents.py.

5. Epsilon Greedy (1 point)
    * Complete the Q-learning agent in qlearningAgents.py by implementing the getAction method implementing epsilon-greedy action selection.
    * You can choose an element from a list by calling random.choice(...) and simulate a binary variable with probability p using util.flipCoin(p).

6. Approximate Q-Learning (2.5 points)
    * Implement the getQValue and update methods in ApproximateQAgent class in qlearningAgents.py.
    * Important: ApproximateQAgent is a subclass of QLearningAgent, for the ApproximateQAgent to work as expected make sure that your methods in QLearningAgent call getQValue instead of accessing the Q-values directly.
