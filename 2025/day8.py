import numpy as np

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
            
def part2(file, num_connections):
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

    # Combine clusters until there is only 1 cluster
    total = 0
    while num_connections < len(distances):
        d = distances[num_connections]
        ids = distance_id_map[d]

        # Search through clusters to find the cluster with ids and combine them
        cluster_id1 = -1
        cluster_id2 = -1
        for i, c in enumerate(clusters):
            if ids[0] in c:
                cluster_id1 = i
            if ids[1] in c:
                cluster_id2 = i

        if cluster_id1 != cluster_id2:
            clusters[cluster_id1].extend(clusters[cluster_id2])
            # Remove one of the original clusters
            clusters.remove(clusters[cluster_id2])

        if len(clusters) == 1:
            total = data[ids[0]][0] * data[ids[1]][0]
            break

        num_connections += 1
    
    print(total)

if __name__=="__main__":
    # file, num_connections = "test_input.txt", 10
    file, num_connections = "input.txt", 1000

    part1(file, num_connections)
    part2(file, num_connections)
