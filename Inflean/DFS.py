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
