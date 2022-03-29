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

#############################################################################

# 두 리스트 합치기
n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
final = list()
p1, p2 = 0, 0
while p1 < n and p2 < m:  # 둘 중 하나가 끝까지가면
    if first[p1] <= second[p2]:
        final.append(first[p1])
        p1 += 1
    else:
        final.append(second[p2])
        p2 += 1
if p1 < n:
    final = final + first[p1:]
else:
    final = final + second[p2:]
for num in final:
    print(num, end=" ")

##############################################################################

# 수들의 합
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
lt, rt = 0, 1
sum_value = numbers[0]
while True:
    if sum_value < m:
        if rt < n:
            sum_value += numbers[rt]
            rt += 1
        else:
            break  # 항상 여기서 break가 걸리게 된다.
    elif sum_value == m:
        cnt += 1
        sum_value -= numbers[lt]
        lt += 1
    else:
        sum_value -= numbers[lt]
        lt += 1
print(cnt)

#############################################################################

# 격자판 최대합
board = list()
n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

max_value = 0
for i in range(n):
    c_sum = 0
    if sum(board[i]) > max_value:  # 행 더하기
        max_value = sum(board[i])

    for j in range(n):  # Column 더하기
        c_sum += board[j][i]
    if c_sum > max_value:
        max_vaule = c_sum

d_sum, d_sum2 = 0, 0

for i in range(n):
    d_sum += board[i][i]
    d_sum2 += board[n - i - 1][i]

if d_sum > max_value:
    max_value = d_sum
elif d_sum2 > max_value:
    max_value = d_sum2

print(max_value)

#############################################################################

# 사과나무 (다이아몬드)
n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]

apple = 0
s = e = n // 2
for i in range(n):
    for j in range(s, e + 1):
        apple += farm[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(apple)

#############################################################################

# 곳감(모래시계)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    r, d, num = map(int, input().split())
    if d == 0:
        for _ in range(num):
            board[r - 1].append(board[r - 1].pop(0))
    else:
        for _ in range(num):
            board[r - 1].insert(0, board[r - 1].pop())

s = 0
e = n - 1
value = 0
for i in range(n):
    for j in range(s, e + 1):
        value += board[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(value)

#############################################################################

# 봉우리
n = int(input())
local = [[0] * (n + 2)]
for i in range(n):
    input_v = list(map(int, input().split()))
    input_v.insert(0, 0)
    input_v.append(0)
    local.append(input_v)
local.append([0 for _ in range(n + 2)])

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(local[i][j] > local[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)

#############################################################################

# 스도쿠 검사
board = [list(map(int, input().split())) for _ in range(9)]
cnt = 0


def check_sudoku(board):
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        for j in range(9):
            check_row[board[i][j]] += 1  # row count
            check_col[board[j][i]] += 1
        if sum(check_row) != 9 or sum(check_col) != 9:
            return False
            break

    for i in range(3):
        for j in range(3):
            check_box = [0] * 10
            for k in range(3):
                for s in range(3):
                    check_box[board[i * 3 + k][j * 3 + s]] += 1
            if sum(check_box) != 9:
                return False
    return True


if check_sudoku == True:
    print("Yes")
else:
    print("No")

#############################################################################

# 격자판 회문수
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(9 // 2):
    for j in range(7):
        number_row = str(board[j][i : i + 5])
        if number_row[::-1] == number_row:
            cnt += 1
# 상하로는 slicing이 불가능
        for k in range(5//2):
            if board[i+k][j]! = board[i+5-k-1][j]
            break
        else:
            cnt+=1

print(cnt)

