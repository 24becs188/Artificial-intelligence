from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Fixed: Changed '-' to '='
    visited.add(start)
    order = []              # Fixed: Moved inside function scope

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        # Fixed: Corrected loop typo and spacing
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Fixed: Changed default value 'none' to capitalized 'None'
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order            # Fixed: Outdented to return after loop finishes

# Example usage
if __name__ == "__main__":  # Fixed: Corrected double underscores

    # Representing graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],    # Fixed: Added missing comma
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Fixed: Standardized curly smart quotes to standard straight quotes
    print("BFS traversal starting from 'A':", bfs(graph, 'A'))
    print("DFS traversal starting from 'A':", dfs(graph, 'A'))
