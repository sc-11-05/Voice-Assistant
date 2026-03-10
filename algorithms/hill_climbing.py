def hill_climbing(options, scores):

    current = options[0]

    for option in options:

        if scores[option] > scores[current]:
            current = option

    return current