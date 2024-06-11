from Puzzle import solve_puzzle
from MST import Prims

def run_tests():
    tests = [
        {
            "puzzle": [['-', '-', '-', '-'], ['-', '-', '-', '-'], ['-', '-', '-', '-']],
            "source": (0, 0),
            "destination": (2, 3),
            "expected_path": [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)],
            "expected_directions_str": "RRRDD"
        },
        {
            "puzzle": [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']],
            "source": (0, 2),
            "destination": (3, 0),
            "expected_path": [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)],
            "expected_directions_str": "LLDDD"
        },
        {
            "puzzle": [['-', '#', '-'], ['-', '#', '-'], ['-', '#', '-']],
            "source": (0, 0),
            "destination": (2, 2),
            "expected_path": None,
            "expected_directions_str": ""
        },
        {
            "puzzle": [['-', '#', '-'], ['-', '#', '-'], ['-', '#', '-']],
            "source": (0, 2),
            "destination": (2, 2),
            "expected_path": [(0, 2), (1, 2), (2, 2)],
            "expected_directions_str": "DD"
        },
        {
            "puzzle": [['-', '#', '-', '-', '-'], ['-', '#', '-', '#', '-'], ['-', '-', '-', '#', '-'], ['#', '#', '#', '-', '-'], ['-', '-', '-', '-', '-']],
            "source": (0, 0),
            "destination": (4, 4),
            "expected_path": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
            "expected_directions_str": "DDRRUURRDDDD"
        },
        {
            "puzzle": [['-', '-', '-', '-', '-'], ['-', '#', '-', '#', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '-', '-', '-', '-']],
            "source": (0, 0),
            "destination": (4, 0),
            "expected_path": [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 0)],
            "expected_directions_str": "DDRDDL"
        },
        {
            "puzzle": [['-', '-', '-', '-', '-']],
            "source": (0, 1),
            "destination": (0, 4),
            "expected_path": [(0, 1), (0, 2), (0, 3), (0, 4)],
            "expected_directions_str": "RRR"
        },
        {
            "puzzle": [['-'], ['-'], ['-'], ['-'], ['-']],
            "source": (3, 0),
            "destination": (0, 0),
            "expected_path": [(3, 0), (2, 0), (1, 0), (0, 0)],
            "expected_directions_str": "UUU"
        },
        {
            "puzzle": [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']],
            "source": (1, 1),
            "destination": (1, 2),
            "expected_path": [(1, 1), (1, 2)],
            "expected_directions_str": "R"
        },
        {
            "puzzle": [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']],
            "source": (1, 1),
            "destination": (1, 1),
            "expected_path": [(1, 1)],
            "expected_directions_str": ""
        },
        {
            "puzzle": [['-', '-', '-', '-', '-'], ['-', '#', '-', '#', '-'], ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-'], ['-', '-', '-', '-', '-']],
            "source": (1, 0),
            "destination": (4, 3),
            "expected_path": [(1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)],
            "expected_directions_str": "DRDDRR"
        },
        {
            "puzzle": [['-', '-', '-', '-', '-'], ['-', '#', '-', '#', '-'], ['-', '#', '-', '-', '-'], ['#', '-', '-', '#', '-'], ['-', '#', '-', '-', '-'], ['-', '-', '-', '-', '-']],
            "source": (2, 0),
            "destination": (4, 0),
            "expected_path": [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (5, 1), (5, 0), (4, 0)],
            "expected_directions_str": "UURRDDDDDLLU"
        },
    ]

    for i, test in enumerate(tests, 1):
        puzzle = test["puzzle"]
        source = test["source"]
        destination = test["destination"]
        expected_path = test["expected_path"]
        expected_directions_str = test["expected_directions_str"]
        
        result = solve_puzzle(puzzle, source, destination)
        
        print(f"Test {i}:")
        print(f"puzzle: {puzzle}")
        print(f"source: {source}")
        print(f"destination: {destination}")
        print(f"expected path: {expected_path}")
        print(f"expected directions_str: {expected_directions_str}")
        print(f"result: {result}")
        print()

run_tests()

def run_tests2():
    tests = [
        {
            "G": [[0, 5], [5, 0]],
            "expected_mst": [(0, 1, 5)]
        },
        {
            "G": [[0, 5, 0], [5, 0, 5], [0, 5, 0]],
            "expected_mst": [(0, 1, 5), (1, 2, 5)]
        },
        {
            "G": [[0, 6, 11, 9], [6, 0, 8, 7], [11, 8, 0, 10], [9, 7, 10, 0]],
            "expected_mst": [(0, 1, 6), (1, 3, 7), (1, 2, 8)]
        },
        {
            "G": [[0, 1, 3, 3, 3], [1, 0, 2, 2, 2], [3, 2, 0, 3, 3], [3, 2, 3, 0, 3], [3, 2, 3, 3, 0]],
            "expected_mst": [(0, 1, 1), (1, 2, 2), (1, 3, 2), (1, 4, 2)]
        },
        {
            "G": [[0, 3, 4, 0, 0], [3, 0, 5, 6, 2], [4, 5, 0, 8, 0], [0, 6, 8, 0, 7], [0, 2, 0, 7, 0]],
            "expected_mst": [(0, 1, 3), (1, 4, 2), (1, 2, 5), (1, 3, 6)]
        },
        {
            "G": [[0, 8, 5, 0, 0, 0, 0], [8, 0, 10, 2, 18, 0, 0], [5, 10, 0, 3, 0, 16, 0], [0, 2, 3, 0, 12, 30, 14], [0, 18, 0, 12, 0, 0, 4], [0, 0, 16, 30, 0, 0, 26], [0, 0, 0, 14, 4, 26, 0]],
            "expected_mst": [(0, 2, 5), (2, 3, 3), (3, 1, 2), (3, 6, 14), (6, 4, 4), (2, 5, 16)]
        },
    ]

    for i, test in enumerate(tests, 1):
        G = test["G"]
        expected_mst = test["expected_mst"]
        
        result_mst = Prims(G)
        
        print(f"Test {i}:")
        print(f"Graph: {G}")
        print(f"Expected MST: {expected_mst}")
        print(f"Result MST: {result_mst}")
        print()

run_tests2()
