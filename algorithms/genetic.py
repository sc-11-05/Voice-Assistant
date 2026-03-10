import random

def genetic_algorithm(options, scores, generations=10):
    population = options[:]
    for _ in range(generations):

        population.sort(key=lambda x: scores[x], reverse=True)
        parents = population[:2]

        child = random.choice(parents)

        if random.random() < 0.2:
            child = random.choice(options)

        population.append(child)

    best = max(population, key=lambda x: scores[x])

    return best