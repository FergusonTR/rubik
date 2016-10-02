#!/usr/bin/python

#   Terry Ferguson & Noah Davis
#   CSC 440
#   Assignment 2: Rubik's Solver


import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    s = start
    parent = {}
    i = 1
    visited = [s]
    answer_path = []
    frontier = [s]
    while frontier:
        next_one = []
        for u in frontier:
            next_adj = []
            next_adj.append(rubik.perm_apply(u, rubik.F))
            next_adj.append(rubik.perm_apply(u, rubik.Fi))
            next_adj.append(rubik.perm_apply(u, rubik.L))
            next_adj.append(rubik.perm_apply(u, rubik.Li))
            next_adj.append(rubik.perm_apply(u, rubik.U))
            next_adj.append(rubik.perm_apply(u, rubik.Ui))
            for v in next_adj:
               if v not in visited:
                    next_one.append(v)
                    visited.append(v)
               if v == end:
                    return answer_path
            frontier = next_one
            answer_path.append(u)
        # print('loop :', i)
        i += 1
    return answer_path


# answer = (shortest_path(rubik.I, rubik.I))
# print (answer)
