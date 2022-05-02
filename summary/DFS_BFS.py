# 조합 구하는 유형 with DFS

# (1) 1~N 까지의 번호가 적힌 구술, 이 중에 M 개를 뽑는 방법의 수


def DFS(v, s):
    global cnt
    if v == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[v] = i
            DFS(v + 1, i + 1)


n, m = 4, 2
cnt = 0
res = [0] * m
DFS(0, 1)
print(cnt)

# (2) - 응용: 수들의 조합 구하기


def DFS(v, start, sum):
    global cnt
    if v == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(start, n):
            DFS(v + 1, i + 1, sum + num[i])


n, k, m = 5, 3, 6
num = [2, 4, 5, 8, 12]
cnt = 0
DFS(0, 0, 0)
print(cnt)

# 최단 거리 통로 구하기

# (1) BFS
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
]
board[0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0


DFS(0, 0)
print(cnt)

# (2) BFS로 풀기
from collections import deque

distance = [[0] * (7) for _ in range(7)]
q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
            board[xx][yy] = 1
            distance[xx][yy] = distance[x][y] + 1
            q.append((xx, yy))

print(distance[6][6])
