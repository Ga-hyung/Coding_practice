# # 상하좌우
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# n = int(input())
# x = 1
# y = 1
# dir = list(input().split())
# for d in dir:
#     if d == "L":
#         xx = x + dx[0]
#         yy = y + dy[0]
#         if 1 <= xx <= n and 1 <= yy <= n:
#             x = xx
#             y = yy
#     elif d == "R":
#         xx = x + dx[1]
#         yy = y + dy[1]
#         if 1 <= xx <= n and 1 <= yy <= n:
#             x = xx
#             y = yy
#     elif d == "U":
#         xx = x + dx[2]
#         yy = y + dy[2]
#         if 1 <= xx <= n and 1 <= yy <= n:
#             x = xx
#             y = yy
#     else:
#         xx = x + dx[3]
#         yy = y + dy[3]
#         if 1 <= xx <= n and 1 <= yy <= n:
#             x = xx
#             y = yy

# print(x, y)

# # 시각
# n = int(input())
# cnt = 0
# for h in range(n + 1):
#     for m in range(60):
#         for s in range(60):
#             if "3" in str(s) + str(m) + str(h):
#                 cnt += 1
# print(cnt)

# # 왕실의 나이트
# start = input()
# x = ord(start[0]) - 96
# y = int(start[1])
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# cnt = 0
# for i in range(len(steps)):
#     xx = x + steps[i][0]
#     yy = y + steps[i][1]
#     if 1 <= xx <= 8 and 1 <= yy <= 8:
#         cnt += 1
# print(cnt)

# 게임 개발
dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

count = 1
turn_time = 0


def turn_left():
    global direction
    direction -= 1  # 90도씩 회전해서 새로운 방향을 바라보게
    if direction == -1:  # 북이면 다시 90도로 회전
        direction = 3


while True:
    turn_left()
    xx = x + dx[direction]
    yy = y + dy[direction]
    if d[xx][yy] == 0 and array[xx][yy] == 0:
        d[xx][yy] = 1
        x = xx
        y = yy
        count += 1
        turn_time = 0
        continue
    # 다 가본 칸이거나, 바다일 경우
    else:
        turn_time += 1
    if turn_time == 4:
        xx = x - dx[direction]
        yy = y - dy[direction]
        if array[xx][yy] == 0:
            x = xx
            y = yy
        else:
            break
        turn_time = 0

print(count)
