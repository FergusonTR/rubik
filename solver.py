#!/usr/bin/python

#   Terry Ferguson & Noah Davis
#   CSC 440
#   Assignment 2: Rubik's Solver


import rubik
from Queue import *


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    i = 0

    if start == end:
        return []

    while not frontier.empty():
        current = frontier.get()

        i+= 1

        if current == end:
            #return values

            break

        neighbors = []
        neighbors.append(rubik.perm_apply(current, rubik.F))
        neighbors.append(rubik.perm_apply(current, rubik.Fi))
        neighbors.append(rubik.perm_apply(current, rubik.L))
        neighbors.append(rubik.perm_apply(current, rubik.Li))
        neighbors.append(rubik.perm_apply(current, rubik.U))
        neighbors.append(rubik.perm_apply(current, rubik.Ui))

        for next in neighbors:
            if next not in came_from:
             frontier.put(next)
             came_from[next] = current

    current = end
    path = [current]
    while current != start:
       current = came_from[current]
       path.append(current)
    path.pop() # pop start, we don't want it i guess
    path.reverse()

    return path

start = rubik.I
middle1 = rubik.perm_apply(rubik.F, start)
middle2 = rubik.perm_apply(rubik.F, middle1)
end = rubik.perm_apply(rubik.Li, middle2)
ans = shortest_path(start, end)

print len(ans)
