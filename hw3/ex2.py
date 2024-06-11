# Dynamic Programming Approach to find distinct ways to arrange blocks to get a total length of N.
def arrange_blocks_dp(N):
    # Initialize an array to store the number of ways to arrange blocks for each length from 0 to N.
    dp = [0] * (N + 1)
    dp[0] = dp[1] = 1
    
    # Iterate over the lengths from 2 to N to compute the number of ways using dynamic programming.
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the total number of distinct arrangements for length N.
    return dp[N]

# Brute Force Approach to find distinct ways to arrange blocks to get a total length of N.
def arrange_blocks_bruteforce(N):
    # Base cases: There is only one way to arrange blocks for length 0 and 1.
    if N == 0 or N == 1:
        return 1
    
    # Recursively explore all possible arrangements.
    return arrange_blocks_bruteforce(N - 1) + arrange_blocks_bruteforce(N - 2)

# Example usage and testing.
N = 3
print("Distinct ways to arrange blocks (Dynamic Programming):", arrange_blocks_dp(N))
print("Distinct ways to arrange blocks (Brute Force):", arrange_blocks_bruteforce(N))
