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

    # print(start)
    # a = rubik.perm_apply(start, rubik.F)
    # b = rubik.perm_apply(a, rubik.Fi)
    # print(a)
    #
    # print(b)

    depth = {s:0}
    parent = {s:None}
    i = 1
    visited = []
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            adj = []
            adj.append(rubik.perm_apply(u, rubik.F))
            adj.append(rubik.perm_apply(u, rubik.Fi))
            adj.append(rubik.perm_apply(u, rubik.L))
            adj.append(rubik.perm_apply(u, rubik.Li))
            adj.append(rubik.perm_apply(u, rubik.U))
            adj.append(rubik.perm_apply(u, rubik.Ui))
            for v in adj:
                if v not in visited:
                    visitv()
				if v not in depth:
					depth[v] = i
					parent[v] = u
					next.append[v]
	    frontier = next
	    i+=1

    return (whatever)

shortest_path(rubik.I, rubik.I)
