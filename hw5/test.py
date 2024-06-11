from Amount import amount
from FeedDog import feedDog

def test_amount(A, S, expected_result):
    result = amount(A, S)
    if result == expected_result:
        print("Test Passed!")
    else:
        print("Test Failed!")
        print("Expected Result:", expected_result)
        print("Actual Result:", result)

'''
# Test Case 1
A1 = [1, 2, 3, 4, 5, 6, 7]
S1 = 10
expected_result1 = [[3, 7], [4, 6], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [1, 2, 3, 4]]
test_amount(A1, S1, expected_result1)

# Test Case 2
A2 = [11, 11, 11, 8, 8, 9, 9, 12, 12]
S2 = 20
expected_result2 = [[8, 12], [9, 11]]
test_amount(A2, S2, expected_result2)

# Test Case 3
A3 = [2, 2, 2, 1, 1, 7, 5]
S3 = 9
expected_result3 = [[2, 7], [1, 1, 7], [2, 2, 5], [1, 1, 2, 5]]
test_amount(A3, S3, expected_result3)

# Test Case 4
A4 = [90, 10, 15]
S4 = 4
expected_result4 = []
test_amount(A4, S4, expected_result4)

# Test Case 5
A5 = [11,1,3,2,6,1,5]
S5 = 8
expected_result5 = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]
test_amount(A5, S5, expected_result5)
'''

# Test cases
test_cases = [
    ([10, 20, 30, 40], [10, 20, 30, 40]),
    ([10, 20, 30], [1, 2, 3]),
    ([3, 13, 5, 15, 12, 28], [30, 1, 5, 3, 14, 10, 2])
]

# Run tests
for i, (hunger_level, biscuit_size) in enumerate(test_cases):
    result = feedDog(hunger_level, biscuit_size)
    print(f"Test case {i+1}: {result} dogs satisfied")

