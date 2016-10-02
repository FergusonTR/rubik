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
    print(start)
    a = rubik.perm_apply(start, rubik.F)
    b = rubik.perm_apply(a, rubik.Fi)
    print(a)

    print(b)

    return

shortest_path(rubik.I, rubik.I)
