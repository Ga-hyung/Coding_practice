# K번째 약수
n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

# K 번째 수
# list 맨 마지막 슬라이싱 번호는 -1 만큼 된 것 까지 출력한다
t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[s - 1 : e]
    numbers.sort()
    print(f"#{i+1}", numbers[k - 1])

#  K번째 큰 수
n, k = map(int, input().split())
card = list(map(int, input().split()))
sum_value = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            sum_value.add(card[i] + card[j] + card[m])
sum_value = sorted(list(sum_value), reverse=True)
print(sum_value[k - 1])
