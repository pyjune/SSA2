# 백준 15683, 카메라가 최대 8대이므로 재귀로도 가능

def f(n, k, N, M):
    global minV
    if n==k: # 모든 카메라에 대한 고려가 끝나면
        cnt = 0
        for i in range(N):
            for j in range(M):
                if office[i][j]==0:
                    cnt += 1
        if cnt<minV:
            minV = cnt
    else:
        r, c, d = cctv[n]
        for m in cam[d]: # 현재 카메라의 가능한 모든 방향
            watch = []
            for x in m: # 정해진 방향을 차례로 꺼냄
                nr = r
                nc = c
                while 0<=nr<N and 0<=nc<M and office[nr][nc]!=6:
                    if office[nr][nc]==0:
                        watch.append((nr,nc))
                        office[nr][nc]= 7 # 추가된 감시영역
                    nr += dr[x]
                    nc += dc[x]
            f(n+1, k, N, M)
            for y in watch:
                office[y[0]][y[1]] = 0 # 감시영역 복원

cam =  [[[0],[1],[2],[3]], # 1번 카메라 방향 설정
        [[0,2],[1,3]],
        [[0,1],[1,2],[2,3],[3,0]],
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        [[0,1,2,3]]]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 1<=office[i][j]<=5:
            cctv.append((i, j, office[i][j]-1)) # 카메라 위치와 종류 기록
minV = 1000
f(0, len(cctv), N, M)
print(minV)
