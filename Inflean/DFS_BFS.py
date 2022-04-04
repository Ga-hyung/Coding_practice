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

##################################################################

# 송아지 찾기(BFS)
