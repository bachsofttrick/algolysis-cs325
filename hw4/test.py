from MaxSet import max_independent_set
from PowerSet import powerset

# Test cases
test_cases = [
    [20, 3, 1, 30, 31, 5, 8],
    [20, 20, 20, 60, 45, 45],
    [90, 90, 0, 0],
    [9, -1, -3, 10, 10],
    [-10, -9, -8, -1, 0, 1, 10, 11, 15],
    [15, 15, 10, -3, -3, -2, 0, 0],
    [19, 23, 90, 91, 5, 9],
    [-9, -7, -19, 0, 0],
    [-1, -1, 0, -10, -34],
    [-1, -1, -2],
    [10, -3, 0]
]

# Run test cases and print results
for i, arr in enumerate(test_cases, 1):
    print(f"Test {i}: {arr}")
    print("Result:", max_independent_set(arr))
    print()

test_cases = [
    [10, 20, 30, 40],
    [55],
    [],
    [-1, -2, -3, 0]
]

for i, test_case in enumerate(test_cases):
    print(f"Test Case {i + 1}: {test_case}")
    print("Powerset:", powerset(test_case))
    print()


