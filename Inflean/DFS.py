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
check = [0] * (n + 1)
total = sum(num)
DFS(0, 0)
print("No")

#################################################################
