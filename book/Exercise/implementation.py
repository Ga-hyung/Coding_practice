# 럭키 스트레이트

n = 7755
num = list()
for i in str(n):
    num.append(int(i))
count1 = 0
count2 = 0
for i in range(len(num)):
    if i < len(num) // 2:
        count1 += num[i]
    else:
        count2 += num[i]
if count1 == count2:
    print("LUCKY")
else:
    print("READY")

# 문자열 압축
word = list("K1KA5CB7")
num = 0
order = list()
for w in word:
    if w.isdecimal():
        num += int(w)
    else:
        order.append(w)
order.sort()
for i in order:
    print(i, end="")
print(num)

# 문자열 압축
s = "abcabcdede"
answer = len(s)
for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step]
    count = 1
    for j in range(step, len(s), step):  # step 길이만큼 계속 이동
        if prev == s[j : j + step]:
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j : j + step]
            count = 1
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
print(answer)

# 자물쇠와 열쇠
def roate_a_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a[0])  # 열
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
n = len(lock)
m = len(key)
new_lock = [[0] * (n * 3) for _ in range(n * 3)]
for i in range(n):  # 중앙에 lock 위치
    for j in range(n):
        new_lock[i + n][j + n] = lock[i][j]
for r in range(4):
    key = roate_a_matrix_by_90_degree(key)
    # new board의 x, y축을 모두 탐색하며 맞는지 찾기
    for x in range(n * 2):
        for y in range(n * 2):
            for i in range(m):  # 열쇠 꼽기
                for j in range(m):
                    new_lock[x + i][y + j] += key[i][j]
            if check(new_lock) == True:
                print("True")
            for i in range(m):  # 열쇠 다시 빼내기
                for j in range(m):
                    new_lock[x + i][y + j] -= key[i][j]
