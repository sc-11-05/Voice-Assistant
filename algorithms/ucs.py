import heapq

def ucs(graph, start, goal):

    queue = [(0, start, [start])]
    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None