import heapq

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

pq = [(0, 1, 0)]  # (cost, node, edges)
dist = {}

while pq:
    cost, node, edges = heapq.heappop(pq)
    
    if node == N:
        print("minimum path weight:", cost)
        break
        
    if edges == K:
        continue
        
    if (node, edges) in dist and dist[(node, edges)] < cost:
        continue
        
    dist[(node, edges)] = cost
    
    for next_node, weight in graph[node]:
        new_cost = cost + weight
        new_edges = edges + 1
        next_state = (next_node, new_edges)
        
        if next_state not in dist or new_cost < dist[next_state]:
            dist[next_state] = new_cost
            heapq.heappush(pq, (new_cost, next_node, new_edges))
else:
    print("minimum path weight: -1")