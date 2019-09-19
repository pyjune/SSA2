di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(lab, N, M):
    global maxV
    f = -1
    r = -1
    q = [0] * N*M*2 # 큐 생성
    visited = [[0]*M for _ in range(N)] # visited 생성
    for i in range(N): # 시작점 인큐 및 visited 표시
        for j in range(M):
            if lab[i][j]==2:
                r += 1
                q[r] = i
                r += 1
                q[r] = j
                visited[i][j] = 1
    while(f!=r): # 큐가 비어있지 않으면 반복
        f += 1 # 디큐
        i = q[f]
        f += 1
        j = q[f]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if lab[ni][nj]==0 and visited[ni][nj]==0: # 인접이면(빈공간이고 바이러스가 퍼지지 않았으면)
                    r += 1
                    q[r] = ni
                    r += 1
                    q[r] = nj
                    visited[ni][nj] = visited[i][j] + 1
    # 모든 칸에 대해 lab[i][j]와 visited[i][j]가 0인 칸 수를 maxV와 비교
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0 and visited[i][j]==0:
                cnt += 1
    if maxV<cnt:
        maxV = cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(N*M-2): # 첫번째 기둥
    if lab[i//M][i%M]==0: 
        for j in range(i+1, N*M-1): # 두번째 기둥
            if lab[j // M][j % M] == 0:
                for k in range(j+1, N*M): # 세번째 기둥
                    if lab[k//M][k%M]==0:
                        lab[i // M][i % M] = 1 # 놓을 수 있는 위치를 확인해 기둥을 세우고
                        lab[j // M][j % M] = 1
                        lab[k // M][k % M] = 1
                        bfs(lab, N, M) # 세균 번식
                        lab[i // M][i % M] = 0  # 기둥 위치를 바꾸기 위해 초기화
                        lab[j // M][j % M] = 0
                        lab[k // M][k % M] = 0
print(maxV)
