di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, N, rain):
    q = []
    q.append((i, j))
    v[i][j] = 1

    while q: # 남은 칸이 있으면
        i, j = q.pop(0)
        for k in range(4): # 주변 칸(4방향)에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] >rain and v[ni][nj] == 0: # 건물이 있고, 표시안한 칸이면
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1

# 전체가 안전영역인 경우 재귀호출의 깊이가 너무 깊어짐. 불가!
def dfs(i, j, N, rain):
    v[i][j] = 1 # 방문표시
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]>rain and v[ni][nj]==0:
                dfs(ni, nj, N, rain)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0 # 전체 강수량에 대한 최대 안전영역 수
for rain in range(100): # 강수량 변화, 각 지역이 1인 경우 강수량 0도 고려해야함
    cnt = 0 # 강수량 별 안전 영역 수
    v = [[0] * N for _ in range(N)]  # 강수량 별로 안전영역 확인
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain and v[i][j]==0: # 강수량 보다 높고 체크되지 않은 곳이면
                cnt += 1  #
                bfs(i, j, N, rain) # i, j칸에 인접한 안전영역 체크
                #dfs(i, j, N, rain)
    if maxV<cnt:
        maxV = cnt
print(maxV)
