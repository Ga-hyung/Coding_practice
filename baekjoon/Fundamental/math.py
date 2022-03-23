# 백준 10430 - 나머지
a, b, c = map(int, input().split())
first = (a + b) % c
second = ((a % c) + (b % c)) % c
third = (a * b) % c
fourth = ((a % c) * (b % c)) % c

print(first)
print(second)
print(third)
print(fourth)

# 백준 4375번 - 1
n = int(input())
for i in range(2, 9999):
    num = int("1" * i)
    if num % n == 0:
        print(len(str(num)))
        break

# 백준 1037번 - 약수
N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
for i in range(N + 1):
    num = numbers[N - 1 - i] * numbers[i]
    if num not in numbers:
        print(num)
        break

# 백준 17427번 문제 - 약수의 합 2
N = int(input())
sum_ = 0
for i in range(1, N + 1):
    sum_ += (N // i) * i
print(sum_)

# 백준 17425번 문제 - 약수의 합
N = int(input())
for i in range(N):
    num = int(input())
    sum_ = 0
    for i in range(1, num + 1):
        sum_ += (n // i) * i
    print(sum_)

# 백준 2609번 - 최대공약수와 최소공배수
a, b = map(int, input().split())
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(max(a, b), a * b):
    if i % a == 0 and i % b == 0:
        print(i)
        break

# 동일한 방법을 유클리드 호제법으로 구현하면 더 간단하게 구현가능
# 재귀함수로 구현
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 최소공배수 공식
# LCM(a,b) = GCD * (a/GCD) * (b/GCD)


# 백준 1978번 - 소수 찾기
N = int(input())
numbers = list(map(int, input().split()))
s_cnt = 0
for num in numbers:
    cnt = 0
    if num == 1:
        continue
    for i in range(2, num // 2):
        if num % i == 0:
            cnt += 1
    if cnt == 1:
        s_cnt += 1
print(s_cnt)

# 백준 1929번 - 소수 구하기
M, N = map(int, input().split())
for num in range(M, N + 1):
    cnt = 0
    for j in range(2, num // 2):
        if num % j == 0:
            cnt += 1
    if cnt == 1:
        print(num)

# 백준 6588번 - 골드바흐의 추측
# 여기서는 에라토스테네스의 체를 사용하면 효과적이다
n = int(input())
check = [True for _ in range(n)]
for i in range(2, n):
    if check[i]:
        for j in range(i + i, n, i):
            check[j] = False

for i in range(3, len(check)):
    if check[i] and check[n - i]:
        print(n, " = ", i, "+", n - i)
        break
