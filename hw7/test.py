from MinPuzzle import minEffort

# Test cases
test_cases = [
    ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 0),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
    ([[1, 3, 5], [2, 8, 3], [3, 4, 5]], 1),
    ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
    ([[1, 2, 2, 3], [3, 8, 2, 5], [5, 3, 4, 8]], 3),
    ([[1, 3, 5], [3, 8, 7], [5, 3, 9], [7, 9, 6]], 3)
]
# Run tests and print results
for i, (puzzle, expected) in enumerate(test_cases):
    result = minEffort(puzzle)
    print('puzzle: ', puzzle)
    print(f"Test {i+1}: {result} (Expected: {expected})")
