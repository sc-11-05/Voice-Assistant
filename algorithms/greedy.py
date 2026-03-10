import heapq

def greedy(graph, start, goal, heuristic):

    queue = [(heuristic[start], start, [start])]
    visited = set()

    while queue:

        h, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            heapq.heappush(queue, (heuristic.get(neighbor, 0), neighbor, path + [neighbor]))

    return None