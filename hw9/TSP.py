import heapq

def solve_tsp(G):
    # Number of nodes in the graph
    n = len(G)
    # Track visited nodes
    visited = [False] * n
    path = []
    current_node = 0
    
    # Helper function to find the nearest unvisited node
    def find_next_node(current_node):
        min_distance = float('inf')
        next_node = -1
        # Loop through all nodes, check if node i is not visited and has the smallest distance
        for i in range(n):
            if not visited[i] and G[current_node][i] > 0 and G[current_node][i] < min_distance:
                min_distance = G[current_node][i]
                next_node = i
        return next_node

    # Start path from the first node
    path.append(current_node)
    visited[current_node] = True

    # Loop through node from 1 to n-1, remove first node 0
    for _ in range(n - 1):
        next_node = find_next_node(current_node)
        if next_node == -1:
            raise Exception("Graph is not fully connected, cannot find a valid TSP path.")
        path.append(next_node)
        visited[next_node] = True
        current_node = next_node
    
    # return to the start node
    path.append(0)
    
    return path

