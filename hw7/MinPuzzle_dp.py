def minEffort(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])

    # Initialize dp array to store minimum effort to reach each cell
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][0] = 0

    # Define directions: right and down
    directions = [(0, 1), (1, 0)]

    # Traverse the puzzle matrix
    for i in range(m):
        for j in range(n):
            # Traverse in both directions: right and down
            for dx, dy in directions:
                x, y = i + dx, j + dy
                # Check if the next cell is within bounds
                if 0 <= x < m and 0 <= y < n:
                    # Update the minimum effort to reach the next cell
                    dp[x][y] = min(dp[x][y], max(dp[i][j], abs(puzzle[x][y] - puzzle[i][j])))

    # Return the minimum effort to reach the destination cell
    return dp[m - 1][n - 1]

# Example usage:
puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print("Output:", minEffort(puzzle))  # Output: 1
