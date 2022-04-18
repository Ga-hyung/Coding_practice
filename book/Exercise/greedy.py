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
