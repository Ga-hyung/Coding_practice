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
