

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
    i = 0
    """Tracking for those nodes visited"""
    visited = [start]
    """my search queue"""
    queue = []
    path =[]
    parent = {start:None}
    count = 0
    queue.append(start)
    while len(queue) > 0:
        count +=1
        """remove the first item from the queue"""
        node = queue.pop(0)
        """Develop each of the child nodes"""
        adj = []
        adj.append(rubik.perm_apply(node, rubik.F))
        adj.append(rubik.perm_apply(node, rubik.Fi))
        adj.append(rubik.perm_apply(node, rubik.L))
        adj.append(rubik.perm_apply(node, rubik.Li))
        adj.append(rubik.perm_apply(node, rubik.U))
        adj.append(rubik.perm_apply(node, rubik.Ui))
        if node == end:
            # path.append(node)
            while parent[node] != None:
                next_one = parent[node]
                path.append(node)
                node = next_one
            path.reverse()
            return path
        for visit in adj:
            if visit not in visited:
                visited.append(visit)
                queue.append(visit)
                parent[visit] = node

"""
start = rubik.I
middle = rubik.perm_apply(rubik.F, start)
end = rubik.perm_apply(rubik.L, middle)
ans = shortest_path(start, end)
print("starting position")
print(start)
print ("ending position")
print(end)
answer =(shortest_path(start, end))
print("answer is")
print (answer)"""