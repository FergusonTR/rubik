import rubik


def solution_path(start_parent, end_parent, found_middle):

    path = []
    path_walk = found_middle
    while start_parent[path_walk] is not None:
        # Insert the answers from the start into the path
        path.insert(0, start_parent[path_walk][1])
        #
        path_walk = start_parent[path_walk][0]
    path_walk = found_middle
    while end_parent[path_walk] is not None:
        path.append(rubik.perm_inverse(end_parent[path_walk][1]))
        path_walk = end_parent[path_walk][0]

    return path


def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.
    Assumes the rubik.quarter_twists move set.
    """
    start_parent = {start: None}
    end_parent = {end: None}
    start_frontier = [start]
    end_frontier = [end]
    twists = rubik.quarter_twists
    if end in start_parent:
        return solution_path(start_parent, end_parent, end)

    for depth in range(7):

        start_next_frontier = []
        end_next_frontier = []
        while len(start_frontier) > 0 or len(end_frontier) > 0:
            start_position = start_frontier.pop()
            end_position = end_frontier.pop()
            for turn in twists:
                start_next_position = rubik.perm_apply(turn, start_position)
                end_next_position = rubik.perm_apply(turn,end_position)
                if start_next_position not in start_parent:
                    start_parent[start_next_position] = (start_position, turn)
                    start_next_frontier.append(start_next_position)
                    if start_next_position in end_parent:
                        return solution_path(start_parent, end_parent, start_next_position)
                if end_next_position not in end_parent:
                    end_parent[end_next_position] = (end_position, turn)
                    end_next_frontier.append(end_next_position)
                    if end_next_position in start_parent:
                        return solution_path(start_parent, end_parent, end_next_position)
        start_frontier = start_next_frontier
        end_frontier = end_next_frontier

    return None

