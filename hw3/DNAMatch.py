'''
Reference:
Top-down and bottom-up codes from the Longest Common Subsequence in Exploration 3.3
https://canvas.oregonstate.edu/courses/1983215/pages/exploration-3-dot-3-dynamic-programming-longest-common-subsequence-problem?module_item_id=24301132
https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bruteforce.py
'''
def dna_match_topdown(DNA1, DNA2):
    # Get the lengths of the DNA sequences.
    m = len(DNA1)
    n = len(DNA2)
    # Initialize a 2D array to store the lengths of common substring parts of DNA1 and DNA2.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    def dna_match_topdown_helper(i, j):
        # Base case: If either of the strings is empty, return 0.
        if i == 0 or j == 0:
            return 0
        # Value exists in dp table
        elif (dp[i][j] != 0):
            return dp[i][j]
        # If the characters at the current positions match, recursively check for the common substring length for the next characters.
        elif DNA1[i - 1] == DNA2[j - 1]:
        	dp[i][j] = 1 + dna_match_topdown_helper(i - 1, j - 1)
        # Recursively branch out and return the maximum of the two branches
        else:
        	dp[i][j] = max(dna_match_topdown_helper(i - 1, j), dna_match_topdown_helper(i, j - 1))
        return dp[i][j]
    
    return dna_match_topdown_helper(m, n)

def dna_match_bottomup(DNA1, DNA2):
    # Get the lengths of the DNA sequences.
    m = len(DNA1)
    n = len(DNA2)
    # Initialize a 2D array to store the lengths of common substring parts of DNA1 and DNA2.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Iterate over the substrings of DNA1 and DNA2 to fill up the dp array.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # i,j have to -1 due to indexes of strings and dp table have a difference of 1 (ie DNA1[0],DNA2[0] is at dp[1][1]).
            if DNA1[i - 1] == DNA2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Return the length of the longest common string alignment found in the bottom right corner of dp array.
    return dp[m][n]

