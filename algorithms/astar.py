from tasks.search_graph import graph
from tasks.heuristic import heuristic
import heapq

def astar(graph, start, goal, heuristic):

    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:

        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph.get(node, []):

            g = cost + weight
            h = heuristic.get(neighbor, 0)

            heapq.heappush(queue, (g + h, g, neighbor, path + [neighbor]))

    return None