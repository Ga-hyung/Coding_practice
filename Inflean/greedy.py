# # 회의실 배정(그리디)
# n = int(input())
# meetings = list()
# for _ in range(n):
#     start, end = map(int, input().split())
#     meetings.append((start, end))
# meetings.sort(key=lambda x: (x[1], x[0]))  # x[1]이 첫 순위, x[0]이 차순으로 정렬

# answer = 0
# et = 0  # 현재 회의 end time
# cnt = 0
# for s, e in meetings:
#     if s >= et:
#         et = e
#         cnt += 1
# if cnt > answer:
#     answer = cnt

# print(answer)

#################################################################

# # 씨름 선수(그리디)
# n = int(input())
# candidate = list()
# for _ in range(n):
#     height, weight = map(int, input().split())
#     candidate.append((height, weight))
# candidate.sort(reverse=True)  # height 로 sort

# max_weight = candidate[0][1]
# cnt = 0
# for h, w in candidate:
#     if w >= max_weight:
#         cnt += 1
#         max_weight = w
# print(cnt)

#################################################################

# # 창고 정리(그리디)
# l = int(input())
# box = list(map(int, input().split()))
# m = int(input())
# box.sort()
# for i in range(m):
#     box[0] += 1
#     box[-1] -= 1
#     box.sort()
# print(box[-1] - box[0])

#################################################################

# # 침몰하는 타이타닉(그리디)
# n, m = map(int, input().split())
# weight = list(map(int, input().split()))
# weight.sort()

# cnt = 0
# while weight:
#     if len(weight) == 1:  # 한명만 남았을 경우
#         cnt += 1
#         break
#     elif weight[0] + weight[-1] > m:
#         cnt += 1
#         weight.pop()
#     else:
#         cnt += 1
#         weight.pop(0)
#         weight.pop()

# print(cnt)

# # list보다 연산이 효율적인 deque로 풀기
# from collections import deque

# n, m = map(int, input().split())
# weight = list(map(int, input().split()))
# weight.sort()
# weight = deque(weight)  # deque화

# cnt = 0
# while weight:
#     if len(weight) == 1:  # 한명만 남았을 경우
#         cnt += 1
#         break
#     elif weight[0] + weight[-1] > m:
#         cnt += 1
#         weight.pop()
#     else:
#         cnt += 1
#         weight.popleft()  # pop(0) 대신해서 popleft로 꺼내기
#         weight.pop()

# print(cnt)

#################################################################

# 증가 수열 만들기(그리디)
