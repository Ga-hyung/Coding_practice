# 모험가 길드

n = 5
ppl = [2, 3, 1, 2, 2]
ppl.sort()
result = 0
count = 0
for x in ppl:
    count += 1
    if count >= x:
        result += 1
        count = 0
print(result)

# 곱하기 혹은 더하기
num = [5, 6, 7]
result = 0
current = num[0]
for n in num[1:]:
    if current * n > current + n:
        result = current * n
        current = current * n
    else:
        result = current + n
        current = current + n
print(result)

# 문자열 뒤집기

s = "0001100"
cnt0 = 0  # 전부 0으로 바꾸는 경우
cnt1 = 0  # 전부 1으로 바꾸는 경우
if s[0] == "1":
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == "1":
            cnt0 += 1
        else:
            cnt1 += 1
print(min(cnt0, cnt1))

# 만들 수 없는 금액
n = 5
coin = [3, 2, 1, 1, 9]
coin.sort()
target = 1  # target 변수를 계속 업데이트 해주는 형식으로 진행해야함
for x in coin:
    if target < x:
        break
    target += x

print(target)

# 볼링공 고르기
n, m = 8, 5
ball = [1, 5, 4, 3, 2, 4, 5, 2]
cnt = 0
for i in range(len(ball)):
    for j in range(i, len(ball)):
        if ball[i] != ball[j]:
            cnt += 1
print(cnt)

# 무지의 먹방 라이브
import heapq

food_times = [8, 6, 4]
k = 15

if sum(food_times) <= k:
    print(-1)
q = []
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i + 1))
sum_value = 0  # 먹기 위해 사용한 시간
previous = 0  # 직전에 다 먹은 음식 시간
length = len(food_times)

while sum_value + ((q[0][0] - previous) * length) <= k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1
    previous = now
result = sorted(q, key=lambda x: x[1])
print(result[(k - sum_value) % length][1])
