def f(i, j, N, M):
    q = []
    q.append((i, j))
    v[i][j] = 1
    while q: # 남은 칸이 있으면
        i, j = q.pop(0)
        for k in range(4): # 주변 칸(4방향)에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if melt[ni][nj] !=0 and v[ni][nj] == 0: # 이웃한 빙산이 있고, 표시안한 빙산이면
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cycle = 0
while True: # 녹은 후 결과를 만들고, 빙산의 개수 확인을 반복
    cycle += 1
    melt = [[0]*M for _ in range(N)] # 녹은 후 결과

    for i in range(N):
        for j in range(M):
            zero = 0
            # for k in range(4):
            #     ni = i + di[k]
            #     nj = j + dj[k]
            #     if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            #         zero += 1
            if j+1<M and arr[i][j+1]==0:
                zero += 1
            if i+1<N and arr[i+1][j]==0:
                zero += 1
            if j-1>=0 and arr[i][j-1]==0:
                zero += 1
            if i-1>=0 and arr[i-1][j]==0:
                zero += 1
            melt[i][j] = arr[i][j]-zero if arr[i][j]>zero else 0
    # 빙산 개수 확인
    cnt = 0;
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if melt[i][j]!=0 and v[i][j]==0:
                cnt += 1
                f(i, j, N, M)
    if cnt!=1:
        break
    for i in range(N):
        for j in range(M):
            arr[i][j] = melt[i][j]

if cnt==0:
    print(0)
else:
    print(cycle)
