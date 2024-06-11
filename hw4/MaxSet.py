def max_independent_set(nums):
    n = len(nums)

    # Initialize an array to store the maximum sum up to each index
    max_sum = [0] * n

    # Base cases
    max_sum[0] = max(0, nums[0])
    if n > 1:
        max_sum[1] = max(max_sum[0], nums[1])

    # Fill the max_sum array using dynamic programming
    for i in range(2, n):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + nums[i])
    
    # Reconstruct the maximum sum subsequence
    max_sum_result = max_sum[n - 1]
    result = []
    i = n - 1
    while i >= 0:
        if i == 0:
            # Append the last element to the result
            if max_sum[i] == nums[i]:
                result.append(nums[i])
            break
        # If the current element's sum is equal to the previous element's sum,
        # move to the previous element
        if max_sum[i] == max_sum[i - 1]:
            i -= 1     
        else:
            # If not, include the current element in the result and move two steps back
            result.append(nums[i])
            i -= 2

    return result[::-1]  # Reverse the result before returning
