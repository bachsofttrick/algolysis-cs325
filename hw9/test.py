from TSP import solve_tsp

def run_tests():
    tests = [
        {
            "G": [[0, 2, 3, 20, 1], [2, 0, 15, 2, 20], [3, 15, 0, 20, 13], [20, 2, 20, 0, 9], [1, 20, 13, 9, 0]],
            "expected_path": [0, 4, 1, 3, 2, 0]
        },
        {
            "G": [[0.0, 1.123, 2.123, 3.123, 4.123], [1.123, 0.0, 2.234, 3.234, 4.234], [2.123, 2.234, 0.0, 3.345, 4.345], [3.123, 3.234, 3.345, 0.0, 4.456], [4.123, 4.234, 4.345, 4.456, 0.0]],
            "expected_path": [0, 1, 2, 3, 4, 0]
        },
        {
            "G": [[0, 5, 3, 0, 1], [5, 0, 9, 8, 2], [3, 9, 0, 7, 0], [0, 8, 7, 0, 4], [1, 2, 0, 4, 0]],
            "expected_path": [0, 4, 1, 2, 3, 0]
        }
    ]

    for i, test in enumerate(tests, 1):
        G = test["G"]
        expected_path = test["expected_path"]
        
        result_path = solve_tsp(G)
        
        print(f"Test {i}:")
        print(f"Graph: {G}")
        print(f"Expected TSP path: {expected_path}")
        print(f"Result TSP path: {result_path}")
        print()

run_tests()
