# 재귀함수를 이용한 이진수 출력


def binary(n):
    if n == 0:
        return
    else:
        binary(n // 2)
        print(n % 2, end="")  # stack이기 때문에 거꾸로 출력된다.


if __name__ == "__main__":
    n = int(input())
    binary(n)

################################################################

# 이진트리순회


def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")  # 전위순회 방식
        DFS(v * 2)  # 왼쪽 자식노드 호툴
        # print(v, end=" ")  # 중위순회
        DFS(v * 2 + 1)  # 오른쪽 자식노드 호출
        # print(v, end=" ")  # 후위순회 - 병합정렬할 때 쓴다


DFS(1)

################################################################

# 부분집합 구하기


def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=" ")
        print()
    else:
        check[v] = 1  # 부분집합으로 사용하는 버전
        DFS(v + 1)
        check[v] = 0  # 부분집합으로 사용하지 않는 버전
        DFS(v + 1)


n = int(input())
check = [0] * (n + 1)
DFS(1)

################################################################

# 합이 같은 부분집합(DFS: 아마존 인터뷰)
import sys


def DFS(L, sum_):
    if sum_ > total // 2:  # 시간 복잡도를 낮추는 방법
        return
    if L == n:
        if sum_ == (total - sum_):
            print("YES")
            sys.exit(0)
    else:
        DFS(L + 1, sum_ + num[L])  # 부분집합에 더한 것
        DFS(L + 1, sum_)  # 부분집합에 더하지 않는 것


n = int(input())
num = list(map(int, input().split()))
total = sum(num)
DFS(0, 0)
print("No")

#################################################################

# 바둑이 승차


def DFS(idx, sum_, tsum):
    global total
    if sum_ + (total - tsum) < result:  # 남아있는 값들을 다 더해도 현재 최대값인 result보다 작으면 내려갈 필요x
        return
    if sum_ > c:
        return
    if idx == n:
        result = max(result, sum_)
    else:
        DFS(idx + 1, sum_ + weight[idx], tsum + weight[idx])
        DFS(idx + 1, sum_, tsum + weight[idx])


c, n = map(int, input().split())
weight = list()
for _ in range(n):
    w = int(input())
    weight.append(w)
result = 0
tsum = sum(weight)
DFS(0, 0, 0)
print(result)

################################################################

# 중복수열 구하기


def DFS(idx):
    global cnt
    if idx == m:  # 중복순열이 완성되었을 떄
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[idx] = i
            DFS(idx + 1)


n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)

#################################################################

# 동전 교환
def DFS(idx, sum_):  # idx는 동전의 갯수
    global res
    if idx > res:  # 제일 작은 count(idx) 값보다 더 크게 나아가지 않도록 막는 것
        return
    if sum_ > m:
        return
    if sum_ == m:
        if idx < res:
            res = idx
    else:
        for i in range(n):
            DFS(idx + 1, sum_ + coin[i])


n = int(input())
coin = list(map(int, input().split()))
m = int(input())
res = 2147000
coin.sort(reverse=True)  # 가장 큰 동전부터 DFS가 시작되므로 효율적이다.
DFS(0, 0)
print(res)

#################################################################

# 순열 구하기


def DFS(v):
    global cnt
    global check
    if v == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if check[i] == 0:

                check[i] = 1
                res[v] = i

                DFS(v + 1)  # 재귀 함수 부르는 부분을 기점으로 끝났을 때 아래 줄에 배치
                check[i] = 0


n, m = map(int, input().split())
res = [0] * m
check = [0] * (n + 1)
cnt = 0
DFS(0)
print(cnt)

################################################################

# 수열 추측하기(순열, 파스칼 응용)

import sys


def DFS(idx, sum_):
    if idx == n and sum_ == f:
        for x in p:
            print(x, end=" ") # 맨 앞에 경우의 수만 print하면 됨
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if check[i] == 0:  # 중복 방지하기
                check[i] = 1
                p[idx] = i  # 순열 만들기
                DFS(idx + 1, sum_ + (p[idx] * b[idx]))
                check[i] = 0  # 재사용이 가능하게


n, f = map(int, input().split())
p = [0] * n
b = [1] * n  # 파스칼 값 계산하기 위한 초기값
check = [0] * (n + 1)  # 순열 만들 때 check list

for i in range(1, n):
    b[i] = (b[i - 1] * (n - i)) // i
DFS(0, 0)

# 라이브러리를 이용해서 푸는 방법
import itertools as it

n, f = map(int, input().split())
b = [1] * n
cnt = 0
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i
num = list(range(1, n + 1))

for tmp in it.permutations(num):  # 모든 경우의 수를 구해준다. (num 중에 3개를 뽑아라)
    sum_ = 0
    for idx, x in enumerate(tmp):
        sum_ += x * b[idx]  # 이걸 누적하기
    if sum_ == f:
        for x in tmp:
            print(x, end=" ")
        break

################################################################

# 조합 구하기 (중요!)


def DFS(v, s):
    global cnt
    if v == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):  # 중복되는 것을 방지하기 위해 s 부터 숫자를 count
            res[v] = i
            DFS(v + 1, i + 1)


# 조합 구하기
n, m = map(int, input().split())
cnt = 0
res = [0] * m
DFS(0, 1)
print(cnt)

################################################################

# 수들의 조합


def DFS(v, start, sum_):
    global cnt
    if v == k:
        if sum_ % m == 0:
            cnt += 1
    else:
        for i in range(start, n):  # num의 list 안에 있는 것 뽑으니까 n+1이 아님
            DFS(v + 1, i + 1, sum_ + num[i])


n, k = map(int, input().split())
num = list(map(int, input().split()))
m = int(input())
cnt = 0
DFS(0, 0, 0)
print(cnt)

# 라이브러리를 이용해 문제 풀기
import itertools as it

n, k = map(int, input().split())
num = list(map(int, input().split()))
m = int(input())
cnt = 0


for tmp in it.combinations(num, k):
    if sum(tmp) % m == 0:
        cnt += 1
print(cnt)

#################################################################

# 인접행렬(가중치 방향 그래프)
n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    n1, n2, weight = map(int, input().split())
    g[n1][n2] = weight

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=" ")
    print()

################################################################

경로 탐색 (그래프 DFS)


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=" ")
        print()
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and check[i] == 0:
                check[i] = 1
                path.append(i)
                DFS(i)  # 이동하는 노드가 되는 것
                check[i] = 0
                path.pop()  # 뒤로 백했을 때는 pop 해줘야함


n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    g[n1][n2] = 1
check = [0] * (n + 1)
check[1] = 1
cnt = 0
path = []
path.append(1)
DFS(1)
print(cnt)
