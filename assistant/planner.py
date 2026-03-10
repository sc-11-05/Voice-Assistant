from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.astar import astar

from tasks.graph import graph
from tasks.weighted_graph import graph as wgraph
from tasks.search_graph import graph as search_graph
from tasks.heuristic import heuristic


def plan_task(action):

    if action == "open_youtube":
        print("Planner: Using Uniform Cost Search")
        return ucs(wgraph, "start", action)

    if action == "find_resume":
        print("Planner: Using A* Search")
        return astar(search_graph, "start", "resume_file", heuristic)

    print("Planner: Using Breadth First Search")
    return bfs(graph, "start", action)