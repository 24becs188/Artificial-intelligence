from queue import PriorityQueue


def best_first_search(graph, start, target, heuristic):
    visited = set()
    pq = PriorityQueue()

    pq.put((heuristic[start], start, [start]))
    visited.add(start)

    while not pq.empty():

        h, node, path = pq.get()

        if node == target:
            return path, h

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))

    return None, None


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': [], 'F': []
    }

    heuristic = {
        'A': 10, 'B': 8, 'C': 5, 'D': 6, 'E': 4, 'F': 0
    }

    path, cost = best_first_search(graph, 'A', 'F', heuristic)
    print(f"Path found by Best First Search: {path} with Target Heuristic: {cost}")
