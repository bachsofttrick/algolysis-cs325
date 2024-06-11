from heapq import heappop, heappush

def solve_puzzle(puzzle, source, destination):
    if source == destination:
        return [source], ''

    # Get the number of rows and columns in the puzzle grid.
    rows, cols = len(puzzle), len(puzzle[0])

    # Define the possible directions of movement and their corresponding row and column changes.
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    
    # Priority queue for Dijkstra's algorithm.
    pq = [(0, source, [], '')]  # (cost, cell, path_so_far, directions_so_far)

    # Set to keep track of visited cells.
    visited = set()
    visited.add(source)

    # Helper function to ensure the next cell is within bounds, not visited, and not an obstacle.
    def is_valid(row, col, cell):
        return 0 <= row < rows and 0 <= col < cols and cell not in visited and puzzle[row][col] == '-'

    # Perform Dijkstra's algorithm to explore the puzzle grid.
    while pq:
        current_cost, current, path_so_far, directions_so_far = heappop(pq)

        # If the destination is reached, return the path and directions.
        if current == destination:
            return (path_so_far + [current], directions_so_far)

        for direction, (dr, dc) in directions.items():
            next_row, next_col = current[0] + dr, current[1] + dc
            next_cell = (next_row, next_col)

            # Ensure the next cell is within bounds, not visited, and not an obstacle.
            if is_valid(next_row, next_col, next_cell):
                new_cost = current_cost + 1
                visited.add(next_cell)
                heappush(pq, (new_cost, next_cell, path_so_far + [current], directions_so_far + direction))
    
    # If the destination is not reached, return None.
    return None
