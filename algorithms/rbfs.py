def rbfs(graph, node, goal, heuristic, cost=0, f_limit=float("inf"), path=None):

    if path is None:
        path = [node]

    if node == goal:
        return path, cost

    successors = []

    for neighbor, weight in graph.get(node, []):

        g = cost + weight
        h = heuristic.get(neighbor, 0)
        f = g + h

        successors.append((f, neighbor, g))

    if not successors:
        return None, float("inf")

    while True:

        successors.sort()
        best_f, best_node, best_cost = successors[0]

        if best_f > f_limit:
            return None, best_f

        alternative = successors[1][0] if len(successors) > 1 else float("inf")

        result, new_f = rbfs(
            graph,
            best_node,
            goal,
            heuristic,
            best_cost,
            min(f_limit, alternative),
            path + [best_node]
        )

        successors[0] = (new_f, best_node, best_cost)

        if result:
            return result, new_f