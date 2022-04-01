from collections import deque

# 공주 구하기 (큐 자료구조로 풀기)

n, k = map(int, input().split())
p = deque(list(range(1, n + 1)))

while p:
    for _ in range(k - 1):  # 1 2
        p.append(p.popleft())
    p.popleft()
    if len(p) == 1:
        print(p[0])
        p.popleft()

#############################################################################

# 응급실 (큐)
n, m = map(int, input().split())
dan = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dan = deque(dan)
cnt = 0
while True:
    cur = dan.popleft()
    if any(cur[1] < x[1] for x in dan):
        dan.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)

#############################################################################

# 교육과정 설계
man = list(input())
n = int(input())

for i in range(n):
    plan = list(input())
    dq = deque(man)  # 과목이 들어올 떄 마다 초기화하기
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print(f"#{i+1} NO")
                break
    else:  # 순서가 통가가 됨
        if len(dq) == 0:
            print(f"{i+1} YES")
        else:
            print(f"{i+1} NO")
