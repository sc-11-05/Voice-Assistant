import random
import math

def simulated_annealing(options, scores, temperature=10, cooling=0.9):

    current = random.choice(options)

    while temperature > 1:

        neighbor = random.choice(options)

        delta = scores[neighbor] - scores[current]

        if delta > 0:
            current = neighbor
        else:
            probability = math.exp(delta / temperature)

            if random.random() < probability:
                current = neighbor

        temperature *= cooling

    return current