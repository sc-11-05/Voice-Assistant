import webbrowser
import os
import urllib.parse

from assistant.optimizer import choose_best_browser
from tasks.app_scores import scores
from assistant.reasoner import reasoning_demo, scheduling_demo
from algorithms.minimax import best_move
from algorithms.genetic import genetic_algorithm
from algorithms.simulated_annealing import simulated_annealing
from algorithms.dls import depth_limited_search
from tasks.graph import graph
from algorithms.iddfs import iddfs
from algorithms.bidirectional import bidirectional_search
from algorithms.rbfs import rbfs
from tasks.search_graph import graph as search_graph
from tasks.heuristic import heuristic


def run_task(task, entity=None):

    if task == "open_browser":

        browser = choose_best_browser()
        print("Best browser:", browser)

        webbrowser.open("https://google.com")

    elif task == "search_google":

        if entity:
            query = urllib.parse.quote(entity)
            webbrowser.open(f"https://www.google.com/search?q={query}")

    elif task == "open_youtube":

        if entity:
            query = urllib.parse.quote(entity)
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            webbrowser.open("https://youtube.com")

    elif task == "open_project":
        os.system("code .")

    elif task == "open_vscode":
        os.system("code")

    elif task == "optimize_browser":

        best = choose_best_browser(scores)
        print("Best browser chosen by AI:", best)

    elif task == "reasoning":

        reasoning_demo()

    elif task == "schedule":

        scheduling_demo()

    elif task == "minimax":

        board = [
            "X","O","X",
            " ","O"," ",
            " "," ","X"
        ]

        move = best_move(board)

        print("Best move for O:", move)
    
    elif task == "genetic":

        options = ["A", "B", "C"]

        scores = {
            "A": 3,
            "B": 7,
            "C": 5
        }

        result = genetic_algorithm(options, scores)

        print("Best option from genetic algorithm:", result)
    
    elif task == "open_website":

        if entity:
            webbrowser.open(f"https://{entity}.com")

    elif task == "annealing":

        options = ["A", "B", "C"]

        scores = {
            "A": 3,
            "B": 7,
            "C": 5
        }

        result = simulated_annealing(options, scores)

        print("Best option from simulated annealing:", result)

    elif task == "dls":

        result = depth_limited_search(graph, "start", "open_project", 3)

        print("DLS path:", result)
    
    elif task == "iddfs":

        result = iddfs(graph, "start", "open_project")

        print("IDDFS path:", result)
    
    elif task == "bidirectional":

        result = bidirectional_search(graph, "start", "open_project")

        print("Bidirectional path:", result)
    
    elif task == "rbfs":

        result, cost = rbfs(search_graph, "start", "resume_file", heuristic)

        print("RBFS path:", result)