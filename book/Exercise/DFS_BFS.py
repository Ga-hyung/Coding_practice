# 특정 거리의 도시 찾기

# n, m, k, x = map(int, input().split())
# INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for z in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])

# check = False
# for i in range(len(graph[x])):
#     if graph[x][i] == k:
#         print(i)
#         check = True

# if check == False:
#     print(-1)

from collections import deque

n, m, k, x = 4, 4, 2, 1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

print(distance)
