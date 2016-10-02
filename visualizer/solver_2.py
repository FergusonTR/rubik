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
	frontier.put(start )
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()

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

	    for next in graph.neighbors(current):
            if next not in came_from:
			 frontier.put(next)
			 came_from[next] = current
	# print(start)
	# a = rubik.perm_apply(start, rubik.F)
	# b = rubik.perm_apply(a, rubik.Fi)
	# print(a)
	#
	# print(b)
	#
	# depth = {s:0}
	# parent = {s:None}
	# i = 1
	# visited = []
	# frontier = [s]
	# while frontier:
	#     next = []
	#     for u in frontier:
	#         adj = []
	#         adj.append(rubik.perm_apply(u, rubik.F))
	#         adj.append(rubik.perm_apply(u, rubik.Fi))
	#         adj.append(rubik.perm_apply(u, rubik.L))
	#         adj.append(rubik.perm_apply(u, rubik.Li))
	#         adj.append(rubik.perm_apply(u, rubik.U))
	#         adj.append(rubik.perm_apply(u, rubik.Ui))
	#         for v in adj:
	#             if v not in visited:
	#                 visitv()
		# 		if v not in depth:
		# 			depth[v] = i
		# 			parent[v] = u
		# 			next.append[v]
	 #    frontier = next
	 #    i+=1

	return a

shortest_path(rubik.I, rubik.I)
