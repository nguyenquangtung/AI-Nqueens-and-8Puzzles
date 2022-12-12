# This is the Test Code for the self-breaking game, solving the 9-tile Puzzle: By IDS . Algorithm
import sys
import random as rd
from random import choice
from collections import deque
import time
import itertools


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # current state of the shape to be folded
        self.parent = parent  # previous state
        self.action = action  # walk ~ 'UP', 'DOWN', 'LEFT', 'RIGHT'
        self.path_cost = path_cost
        self.depth = 0  # current depth
        if parent:
            self.depth = parent.depth + 1

    def Expand(self, problem):  # The set of child nodes is born
        """Returns a list of child Nodes spawned with the corresponding Action-steps"""
        return [self.Child_Node(problem, action) for action in problem.action(self.state)]

    def Child_Node(self, problem, action):  # Khởi tạo node con kế tiếp
        """Returns a ChildNode-Child Node created when performing Action"""
        next_state = problem.Result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(
            self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):  # chuỗi action
        """Output an ordered list of actions leading to the current node state"""
        return [node.action for node in self.path()[1:]]

    def path(self):  # đường đi
        """Output a list of traversed nodes leading to the current node state"""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


def Depth_Limit_Search(node, problem, limit):
    frontier = list([node])     # LIFO
    explored = list()           # contains the explored statuses
    explored_depth = list()     # contains the depth of the explored statuses

    while frontier:
        node = frontier.pop()
        if node.state not in explored:
            explored.append(node.state)
            explored_depth.append(node.depth)
        if problem.goal_test(node.state):
            return node
        else:
            for child in node.Expand(problem):
                if child.depth <= limit:          # 1. Current depth does not exceed Limit
                    if child not in frontier:                   # 2. not in frotier
                        if child.state not in explored:         # 3. not in explored
                            if problem.goal_test(child.state):
                                return child
                            else:
                                # push child in frontier
                                frontier.append(child)
                        elif explored_depth[explored.index(child.state)] > child.depth:
                            explored_depth[explored.index(
                                child.state)] = child.depth
                            if problem.goal_test(child.state):
                                return child
                            else:
                                # push child in frontier
                                frontier.append(child)
                else:
                    break
    return None


def IDLS(problem, node):
    depthlimit = 0
    # Use itertools to run the endless loop
    for depthlimit in itertools.count():
        result = Depth_Limit_Search(node, problem, limit=depthlimit)
        if result != None:
            break
    return result


class EightPuzzleProblem:
    def __init__(self, initial, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
        self.initial = initial  # trạng thái ban đầu
        self.goal = goal  # trạng thái đích

    def action(self, state):  # các action có thể thực hiện
        """Returns the sequence of actions that can be performed in the current State"""
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        # Xóa bớt các nước đi bị hạn chế
        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def goal_test(self, state):
        """Returns True if the current State-state matches Goal-target-state"""
        return state == self.goal

    def find_blank_square(self, state):
        """Returns position of empty cell-zero in State"""
        return state.index(0)

    def Result(self, state, action):
        """In current State perform Action to get new State
         Returns New-new_state"""
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        # tráo đổi 2 trạng thái (di chuyển ô trắng)
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]
        return tuple(new_state)


def random(problem, random_level):
    """Return a Node with any state"""
    x = rd.randint(20, random_level)
    node = Node(problem.goal)
    exlored = set()
    exlored.add(node.state)
    while x > 0:
        temp = choice(node.Expand(problem))
        while temp.state in exlored:
            temp = choice(node.Expand(problem))
        node = temp
        exlored.add(node)
        x = x - 1
    return node


def solve(initialState):
    problem = EightPuzzleProblem(
        initial=None, goal=(0, 1, 2, 3, 4, 5, 6, 7, 8))
    problem.initial = initialState

    node = Node(problem.initial)

    start = time.time()
    result = IDLS(problem, node)
    end = time.time()

    yield result.solution()
    yield end-start


if __name__ == '__main__':
    problem = EightPuzzleProblem(
        initial=(1, 8, 2, 3, 0, 5, 4, 7, 6), goal=(0, 1, 2, 3, 4, 5, 6, 7, 8))
    node = Node(problem.initial)
    result = IDLS(problem, node)
    print(result.solution())
