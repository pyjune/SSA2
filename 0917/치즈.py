def f(N, M): # 가장자리 외부공기 표시
    q = []
    q.append((0, 0))
    v = [[0]*M for _ in range(N)]
    cnt = 0
    while q:
        i, j = q.pop(0)

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj]==0 and v[ni][nj]==0: # 외부공기 확인
                    q.append((ni, nj))
                    v[ni][nj] = 1
                if arr[ni][nj] == 1 and v[ni][nj]==0:  # 외부공기옆 초콜릿
                    cnt += 1
                    arr[ni][nj] = 0
                    v[ni][nj] = 1
    return cnt

# 각 탐색에서 녹은 치즈의 개수 확인 필요
# 탐색에서 녹은 치즈의 개수가 0이면 중단
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pre = 0
turn = 0
while True:
    melt = f(N, M)
    if melt==0:
        break
    pre = melt
    turn += 1
print(turn)
print(pre)
