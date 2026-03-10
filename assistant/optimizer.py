from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from algorithms.genetic import genetic_algorithm
from tasks.app_scores import scores

def choose_best_browser():

    options = list(scores.keys())

    return hill_climbing(options, scores)