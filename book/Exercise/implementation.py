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

# 뱀
n, k = 6, 3
apple = [(3, 4), (2, 5), (5, 3)]
l = 3
info = [(3, "D"), (15, "L"), (17, "D")]
board = [[0] * (n + 1) for _ in range(n + 1)]
for x, y in apple:
    board[x - 1][y - 1] = 1
# 동, 남, 서, 북 (동쪽부터 시작)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    board[x][y] = 2  # 뱀이 있는 위치를 2로 표시
    time = 0
    direction = 0  # 처음에 동쪽을 보고 있을 떄
    index = 0  # 다음 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있는 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0  # 한 칸 이동 한 후, 꼬리 있는 부분 지우기
            # 사과가 있다면 이동 후 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())

# 기둥과 보 설치
n = 5
build_frame = [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1],
]


def possible(answer):
    for x, y, a in answer:
        if a == 0:  # 설치된 것이 기둥 인 경우
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 정상
            if (
                y == 0
                or [x - 1, y, 1] in answer
                or [x, y, 1] in answer
                or [x, y - 1, 0] in answer
            ):
                continue
            return False
        elif a == 1:  # 설치되는 것이 보인 경우
            if (
                [x, y - 1, 0] in answer
                or [x + 1, y - 1, 0] in answer
                or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)
            ):
                continue
            return False
    return True


result = []
for x, y, a, b in build_frame:
    if b == 1:
        result.append([x, y, a])
        if not possible(result):
            result.remove([x, y, a])
    else:
        result.remove([x, y, a])
        if not possible(result):
            result.append([x, y, a])

result.sort()
print(result)

# 치킨 배달
from itertools import combinations

n, m = 5, 2
city = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2],
]
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

candidate = list(combinations(chicken, m))


def get_sum(candidate):
    total = 0
    for i in range(len(house)):
        length = 99999
        x, y = house[i][0], house[i][1]
        for nx, ny in candidate:
            l = abs(x - nx) + abs(y - ny)
            length = min(l, length)
        total += length
    return total


result = 1e9
for c in candidate:
    result = min(result, get_sum(c))
print(result)
