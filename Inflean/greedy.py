# 회의실 배정(그리디)
n = int(input())
meetings = list()
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))  # x[1]이 첫 순위, x[0]이 차순으로 정렬

answer = 0
et = 0  # 현재 회의 end time
cnt = 0
for s, e in meetings:
    if s >= et:
        et = e
        cnt += 1
if cnt > answer:
    answer = cnt

print(answer)

################################################################

# 씨름 선수(그리디)
n = int(input())
candidate = list()
for _ in range(n):
    height, weight = map(int, input().split())
    candidate.append((height, weight))
candidate.sort(reverse=True)  # height 로 sort

max_weight = candidate[0][1]
cnt = 0
for h, w in candidate:
    if w >= max_weight:
        cnt += 1
        max_weight = w
print(cnt)

################################################################

# 창고 정리(그리디)
l = int(input())
box = list(map(int, input().split()))
m = int(input())
box.sort()
for i in range(m):
    box[0] += 1
    box[-1] -= 1
    box.sort()
print(box[-1] - box[0])

################################################################

# 침몰하는 타이타닉(그리디)
n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

cnt = 0
while weight:
    if len(weight) == 1:  # 한명만 남았을 경우
        cnt += 1
        break
    elif weight[0] + weight[-1] > m:
        cnt += 1
        weight.pop()
    else:
        cnt += 1
        weight.pop(0)
        weight.pop()

print(cnt)

# list보다 연산이 효율적인 deque로 풀기
from collections import deque

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)  # deque화

cnt = 0
while weight:
    if len(weight) == 1:  # 한명만 남았을 경우
        cnt += 1
        break
    elif weight[0] + weight[-1] > m:
        cnt += 1
        weight.pop()
    else:
        cnt += 1
        weight.popleft()  # pop(0) 대신해서 popleft로 꺼내기
        weight.pop()

print(cnt)

################################################################

# 증가 수열 만들기(그리디)

from collections import deque

n = int(input())
num = list(map(int, input().split()))
order = list()
lt = 0
rt = n - 1
last = 0
answer = ""
while lt <= rt:
    if num[lt] > last:
        order.append((num[lt], "L"))
    if num[rt] > last:
        order.append((num[rt], "R"))
    order.sort()
    if len(order) == 0:
        break
    else:
        answer = answer + order[0][1]
        last = order[0][0]
        if order[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    order.clear()

print(len(answer))
print(answer)

#################################################################

# 역수열(그리디)
n = int(input())
num = list(map(int, input()))
seq = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if num[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:  # 앞에 seq자리가 비어 있어야 num 을 줄인다
            num[i] -= 1
for x in seq:
    print(x, end=" ")
