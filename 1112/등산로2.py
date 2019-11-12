# 깎지않고 등산로를 만들때의 길이
#1 5
#2 2
#3 5
#4 4
#5 2
#6 10
#7 4
#8 5
#9 9
#10 14

def f(i, j, c, e):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global N
    global K
    global maxV
    # 방문한 칸에 대해
    if maxV<e: # 방문 칸을 포함한 등산로의 최대길이 비교
        maxV = e
    #visited[i][j] = 1 # 등산로에 포함되었음을 표시 (깎음 방지)
    # 주변칸을 탐색
    for m in range(4):
        ni = i + di[m]
        nj = j + dj[m]
        if ni>=0 and ni<N and nj>=0 and nj<N: # 유효 좌표인지 확인
            if arr[i][j]>arr[ni][nj]:
                f(ni, nj, c, e+1)       # 주변의 낮은칸으로 이동
    #visited[i][j] = 0 # 다른 경로의 등산로에 포함될 수 있으므로 해제


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    h = 0 # 등산로의 시작 높이 결정
    for i in range(N):
        for j in range(N):
            if h<arr[i][j]:
                h = arr[i][j]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==h:
                f(i, j, 1, 1) # 좌표i, j, 남은 깎음 횟수, 등산로 길이

    print('#{} {}'.format(tc, maxV))
