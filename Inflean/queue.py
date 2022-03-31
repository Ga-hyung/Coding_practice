from collections import deque

# # 공주 구하기 (큐 자료구조로 풀기)

# n, k = map(int, input().split())
# p = deque(list(range(1, n + 1)))

# while p:
#     for _ in range(k - 1):  # 1 2
#         p.append(p.popleft())
#     p.popleft()
#     if len(p) == 1:
#         print(p[0])
#         p.popleft()

############################################################

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
