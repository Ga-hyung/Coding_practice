# # 거스름돈

# n = 1400
# coin = [500, 100, 50, 10]
# cnt = 0
# for c in coin:
#     cnt += n // c
#     n %= c
# print(cnt)

# # 큰 수의 법칙
# n, m, k = map(int, input().split())
# num = list(map(int, input().split()))
# num.sort(reverse=True)  # 큰 수 부터 정렬
# total = 0
# while m != 0:
#     total += num[0] * k
#     m -= k
#     total += num[1]
#     m -= 1
# print(total)

# # 숫자 카드 게임

# n, m = map(int, input().split())
# card = list()
# for _ in range(n):
#     card.append(list(map(int, input().split())))
# max_card = -21470000
# for i in range(n):
#     if min(card[i]) > max_card:
#         max_card = min(card[i])
# print(max_card)

# 1이 될 때 까지

n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
