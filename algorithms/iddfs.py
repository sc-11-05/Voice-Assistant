def dls(graph, node, goal, depth, path):

    if node == goal:
        return path

    if depth <= 0:
        return None

    for neighbor in graph.get(node, []):

        result = dls(graph, neighbor, goal, depth - 1, path + [neighbor])

        if result:
            return result

    return None

def iddfs(graph, start, goal, max_depth=10):

    for depth in range(max_depth):

        result = dls(graph, start, goal, depth, [start])

        if result:
            return result

    return None