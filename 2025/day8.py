import numpy as np

def get_largest_n_indices_2d(arr, n):
    """
    Returns the 2D indices of the n largest elements in a 2D NumPy array.

    Args:
        arr (np.ndarray): The input 2D NumPy array.
        n (int): The number of largest elements to find.

    Returns:
        tuple: A tuple containing two NumPy arrays: (row_indices, col_indices).
    """
    if n <= 0:
        return np.array([]), np.array([])
    
    # Flatten the array
    flat_arr = arr.flatten()

    # Get the indices of the n largest elements in the flattened array
    # np.argpartition returns indices that would sort the array.
    # We take the last n elements as they correspond to the largest values.
    flat_indices = np.argpartition(flat_arr, -n)[-n:]

    # Convert the flattened indices back to 2D indices
    row_indices, col_indices = np.unravel_index(flat_indices, arr.shape)

    return row_indices, col_indices

def part1(file, num_connections):
    with open(file, 'r') as f:
        data = f.readlines()
    
    for i, line in enumerate(data):
        vals = line.split(',')
        vals2 = [int(v) for v in vals]
        data[i] = vals2
    
    distance_id_map = {}
    distances = []
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            d = np.linalg.norm(np.array(data[i]) - np.array([data[j]]))
            distances.append(d)
            distance_id_map[d] = [i, j]
    
    distances.sort()
    graph = {i:[] for i in range(len(data))} 
    for i in range(num_connections):
        d = distances[i]
        ids = distance_id_map[d]
        graph[ids[0]].append(ids[1])
        graph[ids[1]].append(ids[0])
    
    # Find the 3 largest subgraphs
    visited = [False for i in range(len(data))]
    clusters = []
    # Do BFS to find clusters
    for i in range(len(data)):
        if visited[i]:
            continue
        stack = [i]
        cluster = []
        while len(stack) > 0:
            id = stack.pop(0)
            if id not in cluster:
                cluster.append(id)
            visited[id] = True
            next_ids = graph[id]
            for val in next_ids:
                if not visited[val]:
                    stack.append(val)
        clusters.append(cluster)
    
    clusters.sort(key=len)

    print(len(clusters[-1]) * len(clusters[-2]) * len(clusters[-3]))
            

if __name__=="__main__":
    # file, num_connections = "test_input.txt", 10
    file, num_connections = "input.txt", 1000

    part1(file, num_connections)
    # part2(file)
