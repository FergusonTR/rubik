

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
    i = 1
    visited = [start]                                   # list of nodes visited
    start_queue = []                                    # start queue
    end_queue = []                                      # end queue
    path = []                                           # used to trace path
    start_parent = {start: None}                        # create a start dictionary
    end_parent = {end: None}                            # create an end dictionary
    start_queue.append(start)                           # add the start node
    end_queue.append(end)                               # add the end node
    twists = rubik.quarter_twists                       # list of twists
    """Discuss the algorithm here"""
    while len(start_queue and end_queue) > 0:           # keep looping until a queue is empty
        """remove the first item from the queue"""
        start_node = start_queue.pop(0)                 # pop a node to explore
        end_node = end_queue.pop(0)                     # pop a node to explore
        for turn in twists:
            next_start_node = rubik.perm_apply(turn,start_node)
            next_end_node = rubik.perm_apply(turn,end_node)
            if next_start_node not in start_parent:
                start_parent[next_start_node] = (start_node, turn)
                start_queue.append(next_start_node)
            if next_end_node not in end_parent:
                end_parent[next_end_node] = (end_node, turn)
                end_queue.append(next_end_node)
            if next_start_node in end_parent or next_end_node in start_parent:                      # terminating condition
                """Unwind the paths and merge them"""
                while end_parent[next_end_node] is not None:
                    pair = end_parent[next_end_node]
                    parent_position = pair[0]
                    move = pair[1]
                    path.append(rubik.perm_inverse(move))
                    next_end_node = parent_position
                next_start_node = path[0]
                while start_parent[next_start_node] is not None:
                    pair = start_parent[next_start_node]
                    parent_position = pair[0]
                    move = pair[1]
                    path.insert(0,move)
                    next_start_node = parent_position
                return path                                 # return answer
            """
            for visit in twists:
                next_visit = rubik.perm_apply(visit)
                if visit not in visited:
                    visited.append(visit)
                    start_parent[visit] = (node,visit)
                    queue.append(visit)
            """
            i += 1

"""Test Run"""
start = rubik.I
middle = rubik.perm_apply(rubik.F, start)
end = rubik.perm_apply(rubik.L, middle)
ans = shortest_path(start, end)



print("starting position")
print(start)
print ("ending position")
print(end)
print("answer is")
print (ans)
print("Test Answer is:")
print(rubik.F,rubik.L)