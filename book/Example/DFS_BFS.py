# 음료수 얼려 먹기

# BFS 로 풀기
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
Q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            board[i][j] = 1
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                        board[x][y] = 1
                        Q.append((x, y))
            cnt += 1
print(cnt)

# DFS로 풀기
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]


def DFS(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if DFS(i, j) == True:
            result += 1
print(result)

# 미로 탈출
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(x, y):
    Q = deque()
    Q.append((x, y))
    while Q:
        tmp = Q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
                maze[x][y] = maze[tmp[0]][tmp[1]] + 1
                Q.append((x, y))
    return maze[n - 1][m - 1]


print(BFS(0, 0))
