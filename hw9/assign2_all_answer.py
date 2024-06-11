import itertools

# Distance matrix
distance_matrix = [
    [0, 2, 3, 20, 1],   # A
    [2, 0, 15, 2, 20],  # B
    [3, 15, 0, 20, 13], # C
    [20, 2, 20, 0, 9],  # D
    [1, 20, 13, 9, 0]   # E
]

# List of nodes
nodes = ['A', 'B', 'C', 'D', 'E']

# Convert node list to indices for easier computation
node_indices = range(len(nodes))

# Function to calculate the total distance of a tour
def calculate_tour_distance(tour, distance_matrix):
    distance = 0
    for i in range(len(tour) - 1):
        distance += distance_matrix[tour[i]][tour[i + 1]]
    # Add distance from last node back to the first node
    distance += distance_matrix[tour[-1]][tour[0]]
    return distance

# Initialize minimum distance and optimal tour
min_distance = float('inf')
optimal_tour = None

# Iterate through all tours that start from A (index 0)
for perm in itertools.permutations(node_indices[1:]):
    tour = (0,) + perm
    current_distance = calculate_tour_distance(tour, distance_matrix)
    print("Tour:", ' → '.join(nodes[i] for i in tour), "Total Distance:", current_distance)
    if current_distance < min_distance:
        min_distance = current_distance
        optimal_tour = tour

# Convert the optimal tour indices back to node labels
optimal_tour_labels = [nodes[i] for i in optimal_tour]

# Output the optimal tour and the minimum distance
print("\nOptimal Tour:", ' → '.join(optimal_tour_labels))
print("Total Distance:", min_distance)
