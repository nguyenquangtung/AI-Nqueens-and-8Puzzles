import sys
from collections import deque
import numpy as np
import random
import math


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        #next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        next_node = Node(next_state, self, action)
        return next_node
# ______________________________________________________________________________


class NQueensProblem:

    def __init__(self, N):
        #self.initial = initial
        self.initial = tuple([-1]*N)  # -1: no queen in that column
        self.N = N

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            # return [(col, row) for row in range(self.N)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def value(self, node):
        """Return (-) number of conflicting queens for a given node"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return -num_conflicts


def schedule(t, k=20, lam=0.005, limit=1000):
    return (k * math.exp(-lam * t) if t < limit else 0)


def simulated_annealing(problem):
    current = Node(problem.initial)  # create current tuple -1 * size
    i = 0
    while i < 1000000:  # loop
        t = schedule(i)
        if (t == 0 or -1 not in current.state):  # stop when t==0 or there is goal
            return current.state  # ( -1 not in state)
        if (current.expand(problem) != []):  # may explain
            n = random.choice(current.expand(problem))  # random child
            deltaE = problem.value(n) - problem.value(current)
            if (deltaE < 0):
                print(1)
            if (deltaE > 0 or math.exp(deltaE // t) > 0.5):  # accept when ratio >0.5
                current = n
        else:  # cannot explain
            current = Node(problem.initial)  # create new node
            i = -1  # back to the loop wit i=0, random again
        i += 1  # increase i


if __name__ == '__main__':
    no_of_queens = 15
    problem1 = NQueensProblem(no_of_queens)
    result1 = simulated_annealing(problem1)

    print(result1)
#
