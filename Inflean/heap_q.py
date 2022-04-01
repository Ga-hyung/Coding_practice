import heapq as hq

# heaq는 최소힙으로 작동한다

# 최소힙

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)

##################################################################

# 최대힙
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))  # 부호를 바꿔서 입력 및 출력을 하면 된다.
    else:
        hq.heappush(a, -n)
