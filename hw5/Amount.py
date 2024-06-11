def amount(A, S):
    # Sort the amount values to optimize backtracking
    A.sort()
    result = []
    
    # Define recursive backtracking function
    def backtrack(combination, start, target):
        # Base case: If the remaining target sum is 0, add the current combination to the result list
        if target == 0:
            result.append(combination[:])
            return
        
        for i in range(start, len(A)):
            # If the current element is too big, jump out of loop and move on to the next combination
            if A[i] > target:
                break
            
            # If the current element is a duplicate and has already been used,
            # skip it to avoid duplicates in combinations
            if i > start and A[i] == A[i - 1]:
                continue
            
            combination.append(A[i])
            backtrack(combination, i + 1, target - A[i]) # Move to next index to avoid reusing element
            combination.pop()
    
    backtrack([], 0, S)
    return result

