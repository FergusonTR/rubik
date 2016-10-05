import rubik


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.
    Assumes the rubik.quarter_twists move set.
    """

    start_parent = {}
    end_parent = {}

    start_frontier = set()
    end_frontier = set()

    start_parent[start] = None
    start_frontier.add(start)

    end_parent[end] = None
    end_frontier.add(end)
    
    if end in start_parent:
        return solution_path(start_parent, end_parent, end)
    
    twists = rubik.quarter_twists
    for i in range(7):

        start_next_frontier = []
        end_next_frontier = []
        while len(start_frontier) or 0 and len(end_frontier) > 0:
            start_position = start_frontier.pop()
            end_position = end_frontier.pop()
            for turn in twists:
                start_next_position = rubik.perm_apply(turn, start_position)
                end_next_position = rubik.perm_apply(turn,end_position)
                if start_next_position not in start_parent:
                    start_parent[start_next_position] = (start_position, turn)
                    start_next_frontier.append(start_next_position)
                if end_next_position not in end_parent:
                    end_parent[end_next_position] = (end_position, turn)
                    end_next_frontier.append(end_next_position)
                    if start_next_position in end_parent:
                        return solution_path(start_parent, end_parent, start_next_position)
                    if end_next_position in start_parent:
                        return solution_path(start_parent, end_parent, end_next_position)
        start_frontier = start_next_frontier
        end_frontier = end_next_frontier

    return None


def solution_path(start_parent, end_parent, found_middle):

    path = []
    path_walk = found_middle
    while start_parent[path_walk] is not None:
        start_node = start_parent[path_walk]
        start_parent_node = start_node[0]
        turn = start_node[1]
        path_walk = start_parent_node
        path.insert(0, turn)
    path_walk = found_middle
    while end_parent[path_walk] is not None:
        end_node = end_parent[path_walk]
        end_parent_node = end_node[0]
        turn = end_node[1]
        inverse_turn = rubik.perm_inverse(turn)
        path_walk = end_parent_node
        path.append(inverse_turn)

    return path
