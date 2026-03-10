def depth_limited_search(graph, node, goal, limit, path=None):

    if path is None:
        path = [node]

    if node == goal:
        return path

    if limit <= 0:
        return None

    for neighbor in graph.get(node, []):

        result = depth_limited_search(
            graph,
            neighbor,
            goal,
            limit - 1,
            path + [neighbor]
        )

        if result:
            return result

    return None