#!/usr/bin/python
#
#
#   Terry Ferguson & Noah Davis
#   CSC 440
#   Assignment 2: Rubik's solver

# This solution was in part assisted by an example discovered at MIT while looking for additional information on
# breadth first searches.  The solution was in fact not optimal in that it did not search from the start and end
# at the same time, whereas this solution integrates many loops and allows for a roughly 150ms - 200ms improvement
# in overall timing which is due to the reduction of one of the invariant loops that in itself contained two loops 
# utilizing loop fusion.

import rubik


def solution_path(start_parent, end_parent, found_middle):
    """
    solution_path - This method allows the path to be unwound from the start and end parent tracking
    arrays it is executed at the termination invariant.
     """
    # Setup our output path
    path = []
    # Grab the middle
    path_walk = found_middle
    while start_parent[path_walk] is not None:
        # Insert the answers from the start into the path
        path.insert(0, start_parent[path_walk][1])
        # Select the next item to be pulled for the path
        path_walk = start_parent[path_walk][0]
    # Grab the middle again
    path_walk = found_middle
    while end_parent[path_walk] is not None:
        # Insert the answers from the end into the path
        path.append(rubik.perm_inverse(end_parent[path_walk][1]))
        # Select the next item to be pulled for the path
        path_walk = end_parent[path_walk][0]

    return path


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.
    Assumes the rubik.quarter_twists move set.
    """

    """
    Initialization Invariant - dictionaries are created to hold the moves as they are discovered whenever
    a quarter turn is made.  At the start of the algorithm the API is passed an cube that may be solved or may not
    be, shortest_path cannot make any assumption on the starting condition. The ending position is also provided upon
    initialization, no assumption can be made that a path can be discovered for any given start->end pairing.
    """
    start_parent = {start: None}
    end_parent = {end: None}
    start_frontier = [start]
    end_frontier = [end]
    twists = rubik.quarter_twists

    """
    Termination (already solved) This is the initial check to see if the cube is already solved therefore
    it may be in a terminating state, the return path would be empty.
    """
    if end in start_parent:
        return solution_path(start_parent, end_parent, end)

    """
    Initialization - As discussed in class the worse case path could be 14. Since we are working from each end
    we set our depth of search to 7 thus preventing a halting problem.
    """
    for depth in range(7):
        # Blank the frontier's to support each loop iteration
        start_next_frontier = []
        end_next_frontier = []
        """
        Maintenance - At this point we are aware that the frontier is being explored, so long as there is more
        """
        while len(start_frontier) > 0 or len(end_frontier) > 0:
            start_position = start_frontier.pop()
            end_position = end_frontier.pop()
			for turn in twists:
                start_next_position = rubik.perm_apply(turn, start_position)
                end_next_position = rubik.perm_apply(turn,end_position)
                if start_next_position not in start_parent:
                    """
                    Maintenance - This documents our search of the frontier we have made progress when the Parent
                    dictionaries are populated however we cannot assume that there is a path to solution only that
                    there are moves that resulted in positions. At this point we cannot make any assumptions
                    on the remaining moves to reach our end solution.
                    """
                    start_parent[start_next_position] = (start_position, turn)
                    start_next_frontier.append(start_next_position)
                    """
                    Termination Invariant - The start search of the frontier has discovered a node already
                    discovered by the end frontier search.
                    """
                    if start_next_position in end_parent:
                        return solution_path(start_parent, end_parent, start_next_position)
                if end_next_position not in end_parent:
                    end_parent[end_next_position] = (end_position, turn)
                    end_next_frontier.append(end_next_position)
                    if end_next_position in start_parent:
                        return solution_path(start_parent, end_parent, end_next_position)
        """
        Maintenance Invariant (explore more) we have not found a solution however we have more nodes to explore
        """
        start_frontier = start_next_frontier
        end_frontier = end_next_frontier
    """
    Termination Invariant - The searching has failed we have exceeded the depth of the worse case search and
    we have prevented a halting problem.
    """
    return None

