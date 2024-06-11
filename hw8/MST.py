import heapq

def Prims(G):
    n = len(G)
    visited = [False] * n

    # Initialize the min-heap with a tuple containing (weight, starting vertex, no parent)
    min_heap = [(0, 0, -1)]  # parent_vertex = -1 for starting vertex
    mst_edges = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        # If the vertex has already been visited, skip to the next iteration
        if visited[u]:
            continue

        visited[u] = True
        # If the parent is valid (i.e., not the starting vertex), add the edge to MST
        if parent != -1:
            mst_edges.append((parent, u, weight))

        for v in range(n):
            # If there's an edge and the vertex v has not been visited
            if G[u][v] != 0 and not visited[v]:
                heapq.heappush(min_heap, (G[u][v], v, u))
    
    return mst_edges

