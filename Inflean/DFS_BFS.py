# 최대점수 구하기(DFS)


def DFS(level, value, time):
    global score
    if time > m:
        return  # 멈추기
    if level == n:
        if value > score:
            score = value
    else:
        DFS(level + 1, value + pv[level], time + pt[level])
        DFS(level + 1, value, time)


n, m = map(int, input().split())
pv = list()
pt = list()
for _ in range(n):
    s, t = map(int, input().split())
    pv.append(s)
    pt.append(t)
score = 0
DFS(0, 0, 0)
print(score)

#################################################################

# 휴가(삼성 SW역량 평가 기출 문제: DFS 활용)


def DFS(level, pay):  # level은 날짜 역시 의미함
    global max_pay
    if level == n + 1:
        if pay > max_pay:
            max_pay = pay
    else:
        if level + ti[level] <= n + 1:
            DFS(level + ti[level], pay + pi[level])
        DFS(level + 1, pay)


n = int(input())
ti = list()
pi = list()
for _ in range(n):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)
max_pay = 0
ti.insert(0, 0)
pi.insert(0, 0)
DFS(1, 0)
print(max_pay)

#################################################################

# 양팔저울(DFS)


def DFS(level, sum_):
    if level == k:
        check[abs(sum_)] = 1
    else:
        DFS(level + 1, sum_ + cho[level])  # 왼쪽에 놓을 때
        DFS(level + 1, sum_ - cho[level])  # 오른쪽에 놓을 때
        DFS(level + 1, sum_)  # 놓지 않을 때


k = int(input())
cho = list(map(int, input().split()))
s = sum(cho)
check = [0] * (s + 1)

DFS(0, 0)
cnt = 0
for i in check:
    if i == 0:
        cnt += 1
print(check)
print(cnt)

#################################################################

# 동전 바꿔주기(DFS)


def DFS(level, sum_):
    global cnt
    if sum_ > T:
        return
    if level == k:
        if sum_ == T:
            cnt += 1
    else:
        for i in range(ni[level] + 1):
            DFS(level + 1, sum_ + pi[level] * i)


T = int(input())
k = int(input())
pi = list()
ni = list()
for _ in range(k):
    p, n = map(int, input().split())
    pi.append(p)
    ni.append(n)
cnt = 0
DFS(0, 0)
print(cnt)

#################################################################

# 동전분배하기(DFS)


def DFS(level):
    global diff
    if level == n:
        if diff > max(money) - min(money):
            tmp = set()
            for x in money:
                tmp.add(x)  # 중복은 제외한다.
            if len(tmp) == 3:
                diff = max(money) - min(money)
    else:
        for i in range(3):
            money[i] += coin[level]
            DFS(level + 1)
            money[i] -= coin[level]  # 백으로 왔을 떄


n = int(input())
coin = list()
for _ in range(n):
    c = int(input())
    coin.append(c)
money = [0] * 3
diff = 2147000
DFS(0)
print(diff)

##################################################################

# 알파코드(DFS)


def DFS(level, p):
    global cnt
    if level == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j] + 64), end=" ")
        print()
    else:
        for i in range(1, 27):
            if code[level] == i:  # i 가 한 자리 수 일 떄
                res[p] = i
                DFS(level + 1, p + 1)
            elif (
                i >= 10 and code[level] == i // 10 and code[level + 1] == i % 10  #
            ):  # code(-1, -1)를 넣었기에 가능, i 가 두 자리 수일 때
                res[p] = i
                DFS(level + 2, p + 1)


code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * (n + 3)
cnt = 0
DFS(0, 0)
print(cnt)

#################################################################

# 송아지 찾기(BFS)

from collections import deque


s, e = map(int, input().split())
dis = list()
Max = 10000
check = [0] * (Max + 1)
dis = [0] * (Max + 1)  # 0 번 부터
check[s] = 1
dis[s] = 0
dQ = deque()
dQ.append(s)  # 출발점 입력

while dQ:
    now = dQ.popleft()  # 부모 값
    if now == e:
        break
    for nex in (now - 1, now + 1, now + 5):  # 차례 차례 튜플값을 탐색
        if 0 < nex <= Max:
            if check[nex] == 0:
                dQ.append(nex)
                check[nex] = 1
                dis[nex] = dis[now] + 1

print(dis[e])  # 도착지점에 몇 번 만에 왔는지 프린트 가능

#################################################################

# 사과나무 (BFS)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
s = e = n // 2
dQ = deque()
dQ.append((s, e))
check[s][e] = 1
total = apple[s][e]
level = 0

while True:
    if level == n // 2:
        break
    size = len(dQ)
    for i in range(size):  # 한 level 탐색 완료
        tmp = dQ.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y] == 0:
                total += apple[x][y]
                check[x][y] = 1
                dQ.append((x, y))
    level += 1
print(total)

#################################################################

# 미로의 최단거리 통로(BFS)
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dQ = deque()
dQ.append((0, 0))
board[0][0] = 1
while dQ:
    tmp = dQ.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1  # check 효과가 나게 벽으로 만들어버린다
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1  # 가는 방법 count
            dQ.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])  # 가는 방법이 어떻게 되는지 count

#################################################################

# 미로탐색(DFS)
# 최단 거리가 아닌 갈 수 있는 방법이 몇 개인지 count하는 문제
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


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
                board[xx][yy] = 0  # 뒤로 백


board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
board[0][0] = 1
DFS(0, 0)
print(cnt)

#################################################################

# 등산경로(DFS)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    if x == ex and y == ey:  # 도착지점에 돌아오면 count
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if (
                0 <= xx < n
                and 0 <= yy < n
                and board[xx][yy] > board[x][y]
                and check[xx][yy] == 0
            ):
                check[xx][yy] = 1
                DFS(xx, yy)
                check[xx][yy] = 0


n = int(input())
board = [[0] * n for _ in range(n)]
check = [[0] * n for _ in range(n)]
cnt = 0
max_ = -2147000
min_ = 2147000
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min_:
            min_ = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max_:
            max_ = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]
check[sx][sy] = 1  # 출발지점 count
cnt = 0
DFS(sx, sy)
print(cnt)

#################################################################

# 단지 번호 붙이기(DFS, BFS)

# DFS로 풀기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    aprt[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and aprt[xx][yy] == 1:
            DFS(xx, yy)


n = int(input())
aprt = [list(map(int, input())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if aprt[i][j] == 1:  # 여기서 부터 DFS 시작
            cnt = 0
            DFS(i, j)
            res.append(cnt)
res.sort()
print(len(res))
for x in res:
    print(x)

# BFS로 풀기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
aprt = [list(map(int, input())) for _ in range(n)]
cnt = 0
res = []
Q = deque()
for i in range(n):
    for j in range(n):
        if aprt[i][j] == 1:
            aprt[i][j] = 0
            Q.append((i, j))
            cnt = 1

            # BFS 돌기
            while Q:  # 주변에 있는 아파트 다 찾기
                tmp = Q.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or aprt[x][y] == 0:
                        continue
                    aprt[x][y] = 0
                    Q.append((x, y))
                    cnt += 1
            res.append(cnt)
print(len(res))
for x in res:
    print(x)

#################################################################

# 섬나라 아일랜드(BFS)

from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]  # 대각선까지 포함
n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]
res = []
Q = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            mapp[i][j] = 0
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and mapp[x][y] == 1:
                        mapp[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)
