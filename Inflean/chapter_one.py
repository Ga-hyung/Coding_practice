# # # K번째 약수
# n, k = map(int, input().split())
# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)

# # # K 번째 수
# # # list 맨 마지막 슬라이싱 번호는 -1 만큼 된 것 까지 출력한다
# t = int(input())
# for i in range(t):
#     n, s, e, k = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     numbers = numbers[s - 1 : e]
#     numbers.sort()
#     print(f"#{i+1}", numbers[k - 1])

# # #  K번째 큰 수
# n, k = map(int, input().split())
# card = list(map(int, input().split()))
# sum_value = set()
# for i in range(n):
#     for j in range(i + 1, n):
#         for m in range(j + 1, n):
#             sum_value.add(card[i] + card[j] + card[m])
# sum_value = sorted(list(sum_value), reverse=True)
# print(sum_value[k - 1])

# # 최솟값 구하는 방법
# arr = [5, 3, 7, 8, 2, 5, 2, 6]
# Min = float("inf")
# for i in range(len(arr)):
#     if arr[i] <= Min:
#         Min = arr[i]

# print(Min)

# 대표값
# N = int(input())
# student = list(map(int, input().split()))
# avg = round(sum(student) / len(student))
# dif = 2147000000
# for i in range(len(student)):
#     if dif > abs(student[i] - avg):
#         dif = abs(student[i] - avg)
#         score = student[i]
#         stud_num = i + 1
#     elif dif == abs(student[i] - avg):
#         if student[i] > score:
#             score = student[i]
#             stud_num = i + 1

# print(avg, stud_num)

# 정다면체
# n, m = map(int, input().split())
# cnt = [0 for _ in range(m + n + 3)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         sum_value = i + j
#         cnt[sum_value] += 1

# for idx, val in enumerate(cnt):
#     if val == max(cnt):
#         print(idx, end=" ")

# 자릿수의 합

# 2가지의 방법 가능
# version 1
# def digit_sum(x):
#     value_sum = 0
#     while x > 0:
#         value_sum += x % 10
#         x = x // 10

#     return value_sum

# # version 2
# def digit_sum_v2(x):
#     value_sum = 0
#     for i in str(x):
#         value_sum+=int(i)

#     return value_sum

# n = int(input())
# numbers = list(map(int, input().split()))
# max_sum = 0
# for i in range(n):
#     if digit_sum(numbers[i]) > max_sum:
#         max_sum = digit_sum(numbers[i])
#         max_value = numbers[i]
# print(max_value)

# 소수 (에라토스테네스 체)
n = int(input())
check = [True for _ in range(n + 1)]
cnt = 0
for i in range(2, n + 1):
    if check[i] == True:
        cnt += 1
        for j in range(i, n + 1, i):
            check[j] = False
print(cnt)
