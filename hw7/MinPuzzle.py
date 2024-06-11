import heapq

def minEffort(puzzle):
    m, n = len(puzzle), len(puzzle[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Helper function to check if a cell is within bounds
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n
    
    # Initialize distances matrix with infinity
    distances = [[float('inf')] * n for _ in range(m)]
    distances[0][0] = 0
    
    # Priority queue to store cells based on their difference
    pq = [(0, 0, 0)]  # (max_diff, x, y)
    
    while pq:
        max_diff, x, y = heapq.heappop(pq)
        
        # Destination reached
        if x == m - 1 and y == n - 1:
            return max_diff
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                # Calculate the difference of the current move
                new_diff = max(max_diff, abs(puzzle[nx][ny] - puzzle[x][y]))
                if new_diff < distances[nx][ny]:
                    distances[nx][ny] = new_diff
                    heapq.heappush(pq, (new_diff, nx, ny))
                    
    # Destination unreachable
    return -1

