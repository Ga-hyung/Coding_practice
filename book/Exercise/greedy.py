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
