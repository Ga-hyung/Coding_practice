# 이분 검색
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
# 이분 검색 알고리즘
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if num[mid] == m:
        print(mid + 1)
        break
    elif num[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

#########################################################################

# 랜선 자르기 (결정알고리즘)
k, n = map(int, input().split())
cable = list()
for _ in range(k):
    c_length = int(input())
    cable.append(c_length)

lt = 1
rt = max(cable)
answer = 0
while lt <= rt:
    cnt = 0
    mid = (lt + rt) // 2  # 랜선의 길이
    for i in cable:
        cnt += i // mid
    if cnt >= n:
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(answer)

#########################################################################

# 뮤직비디오(결정알고리즘)
def slice_songs(minute):
    sum_songs = 0
    cnt = 1
    for i in range(n):
        if sum_songs + songs[i] > minute:
            cnt += 1
            sum_songs = songs[i]  # 초기화
        else:
            sum_songs += songs[i]
    return cnt


n, m = map(int, input().split())
songs = list(map(int, input().split()))

max_song = max(songs)

lt = 1
rt = sum(songs)
answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = slice_songs(mid)
    if max_song <= mid and cnt <= m:
        answer = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(answer)

##########################################################################

# 마구간 정하기(결정 알고리즘)


def count_horse(length):
    cnt = 1
    h = line[0]
    for x in line:
        if x - h >= length:
            cnt += 1
            h = x

    return cnt


n, c = map(int, input().split())
line = list()
for _ in range(n):
    x = int(input())
    line.append(x)
line.sort()

lt = 1
rt = line[-1]
answer = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if count_horse(mid) >= c:
        answer = mid
        lt = mid + 1  # 최대 거리를 찾고자 하니 작은 값 날리기
    else:
        rt = mid - 1
print(answer)
