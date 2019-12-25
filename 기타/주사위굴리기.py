# 백준 14499

dr = [0, 0, 0, -1, 1] #동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dc = [0, 1, -1, 0, 0]

dice = [0]*6
opposite = [5, 4, 3, 2, 1, 0]
N, M, r, c, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
i = 5
for j in cmd: #동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    nr = r+dr[j]
    nc = c+dc[j]
    if 0<=nr<N and 0<=nc<M:
        if j==1: #동쪽
            t = dice[2]
            dice[2] = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = t
        elif j==2: # 서쪽
            t = dice[3]
            dice[3] = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = t
        elif j==3: # 북쪽
            t = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = t
        elif j==4: # 남쪽
            t = dice[4]
            dice[4] = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = t
        if A[nr][nc]==0:
            A[nr][nc] = dice[5] # 주사위 숫자를 복사
        else:
            dice[5] = A[nr][nc] # 바닥면 숫자 옮김
            A[nr][nc] = 0
        print(dice[0]) # 바닥 반대면(윗면)의 숫자
        r, c = nr, nc
