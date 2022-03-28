# 회문 문자열 검사
n = int(input())
for i in range(n):
    word = input()
    word = word.lower()
    if word[::-1] == word:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

##############################################################################

# 숫자만 추출
# version 1
import re

word = input()
word = re.sub(r"[^0-9]", "", word)
word = int(word)
cnt = 0
for i in range(1, word + 1):
    if word % i == 0:
        cnt += 1
print(word)
print(cnt)

# version 2
word = input()
res = 0
for x in word:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)

##############################################################################

# 카드 역배치(정올 기출)
card = [i for i in range(1, 21)]
for i in range(10):
    a, b = map(int, input().split())
    reverse = card[a - 1 : b][::-1]
    card[a - 1 : b] = reverse
    # for j in range((b - a + 1) // 2):
    #     card[a + j], card[b - j] = card[b - j], card[a + j] # 이런 방식으로 풀어도 된다
card.pop(0)
for num in card:
    print(num, end=" ")
