from collections import deque

def bidirectional_search(graph, start, goal):

    if start == goal:
        return [start]

    front_queue = deque([(start, [start])])
    back_queue = deque([(goal, [goal])])

    front_visited = {start: [start]}
    back_visited = {goal: [goal]}

    while front_queue and back_queue:

        node, path = front_queue.popleft()

        for neighbor in graph.get(node, []):

            if neighbor not in front_visited:

                new_path = path + [neighbor]
                front_visited[neighbor] = new_path
                front_queue.append((neighbor, new_path))

                if neighbor in back_visited:
                    return new_path + back_visited[neighbor][-2::-1]


        node, path = back_queue.popleft()

        for neighbor in graph.get(node, []):

            if neighbor not in back_visited:

                new_path = path + [neighbor]
                back_visited[neighbor] = new_path
                back_queue.append((neighbor, new_path))

                if neighbor in front_visited:
                    return front_visited[neighbor] + new_path[-2::-1]

    return None