# 네트워크 선 자르기(Bottom-Up)

# f(n) = f(n-2) + f(n-1)
n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])

# 네트워크 선 자르기(Top-Down: 재귀, 메모이제이션)


def DFS(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1 or n == 2:  # 종착점일 떄
        return n
    else:
        dy[n] = DFS(n - 1) + DFS(n - 2)
        return dy[n]


n = int(input())
dy = [0] * (n + 1)  # 메모이제이션 하는 배열
print(DFS(n))

#################################################################

# 계단 오르기(Top-Down: 메모이제이션)


def DFS(n):
    if n == 1 or n == 2:
        return n
    if dy[n] > 0:
        return dy[n]
    else:
        dy[n] = DFS(n - 1) + DFS(n - 2)
        return dy[n]


n = int(input())
dy = [0] * (n + 1)
print(DFS(n))


# 계단오르기(Bottom Up)

n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])

#################################################################

# 돌다리 건너기(Bottom-Up)

n = int(input())
dy = [0] * (n + 2)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 2):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n + 1])

# 돌다리 건너기(Top-Down)


def DFS(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1 or n == 2:
        return n
    else:
        dy[n] = DFS(n - 1) + DFS(n - 2)
        return dy[n]


n = int(input())
dy = [0] * (n + 2)
print(DFS(n + 1))

################################################################

# 최대 부분 증가수열(LIS: Longest Increasing Subsequence)

n = int(input())
num = list(map(int, input().split()))
dy = [0] * (n + 1)
dy[1] = 1
res = 0
for i in range(2, n + 1):
    max_ = 0  # 갈 수 있는 방법 count 시작
    for j in range(i - 1, 0, -1):  #
        if num[j] < num[i] and dy[j] > max_:  # 앞에 항이 작아야한다.
            max_ = dy[j]
    dy[i] = max_ + 1
    if dy[i] > res:
        res = dy[i]
print(res)

#################################################################

# 최대 선 연결하기

n = int(input())
num = list(map(int, input().split()))
num.insert(0, 0)
dy = [0] * (n + 1)
res = 0
dy[1] = 1
for i in range(2, n + 1):
    max_ = 0
    for j in range(i - 1, 0, -1):
        if num[j] < num[i] and dy[j] > max_:
            max_ = dy[j]
    dy[i] = max_ + 1
    if dy[i] > res:
        res = dy[i]
print(res)

################################################################

# 가장 높은 탑 쌓기

n = int(input())
brick = []
for _ in range(n):
    l, h, w = map(int, input().split())
    brick.append((l, h, w))
brick.sort(reverse=True)  # 밑면 넓비에 의해 내림차순 정렬
dy = [0] * (n)
dy[0] = brick[0][1]
res = brick[0][1]

for i in range(1, n):
    max_height = 0
    for j in range(i - 1, -1, -1):
        if brick[j][2] > brick[i][2] and dy[j] > max_height:
            max_height = dy[j]
    dy[i] = max_height + brick[i][1]

    if dy[i] > res:
        res = dy[i]
print(res)

################################################################

# 알리바바와 40인의 도둑(Bottom-Up)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]
dy[0][0] = board[0][0]

for i in range(1, n):  # 초기화
    dy[0][i] = dy[0][i - 1] + board[0][i]
    dy[i][0] = dy[i - 1][0] + board[i][0]
for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i - 1][j], dy[i][j - 1]) + board[i][j]
print(dy[n - 1][n - 1])

# 알리바바와 40인의 도둑(Top-Down)


def DFS(x, y):
    if x == 0 and y == 0:
        return board[0][0]
    if dy[x][y] > 0:
        return dy[x][y]
    else:
        if y == 0:
            dy[x][y] = DFS(x - 1, y) + board[x][y]
            return DFS(x - 1, y) + board[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y - 1) + board[x][y]
        else:  # 두갈래 길 인 지점
            dy[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + board[x][y]
        return dy[x][y]


n = int(input())
board = [list(map(int, input().split()))]
dy = [[0] * n for i in range(n)]
print(DFS(n - 1, n - 1))

################################################################

# 가방문제(Knapsack Algorithm)

n, m = map(int, input().split())
dy = [0] * (m + 1)  # 가방에 j무게 보석의 최대 가치
for _ in range(n):
    w, v = map(int, input().split())
    for j in range(w, m + 1):
        if dy[j - w] + v > dy[j]:
            dy[j] = dy[j - w] + v
print(dy[m])

################################################################

# 동전교환(Knapsack Algorithm)
n = int(input())
coin = list(map(int, input().split()))
cost = int(input())
dy = [1000] * (cost + 1)  # j원을 거슬러 주는데 사용된 동전의 최소 개수
dy[0] = 0
for c in coin:
    for j in range(c, cost + 1):
        dy[j] = min(dy[j - c] + 1, dy[j])
print(dy[cost])

#################################################################

# 최대점수 구하기(Knapsack Algorithm)
# 한 문제만 풀 수 있다는 제한 조건이 존재

n, l = map(int, input().split())
dy = [0] * (l + 1)  # j시간을 안에 풀 수 있는 최대 점수
for i in range(n):
    ps, pt = map(int, input().split())
    for j in range(l, pt - 1, -1):
        dy[j] = max(dy[j], dy[j - pt] + ps)
print(dy[l])

#################################################################
