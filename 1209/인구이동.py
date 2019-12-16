def bfs(u, i, j, N, L, R): # 연합 찾기
    q = []
    q.append((i, j))
    union[i][j] = u
    ulist = []
    while q:
        i, j = q.pop(0)
        ulist.append((i, j))
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if union[ni][nj]==0 and L<=abs(p[ni][nj]-p[i][j])<=R: # 아직 연합에 속하지 않고 인구범위이내면
                    union[ni][nj] = u # 국경을 열어 연합에 포함시키고
                    q.append((ni, nj)) # 탐색 계속
    # 연합의 인구구하기
    if len(ulist)>=2: # 연합에 속한 나라가 2개 이상이면
        s = 0
        for pos in ulist:
            s += p[pos[0]][pos[1]] # 각 나라의 인구 합계
        s //= len(ulist)  #연합에 속한 나라수로 나눈 평균
        for pos in ulist:
            p[pos[0]][pos[1]] = s
        return 1
    return 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


N, L, R = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]

cnt = 0 # 인구이동 횟수
r = 1 # 각 탐색 단계에서의 인구이동 횟수(연합의 개수)
while r>0:
    union = [[0]*N for _ in range(N)]
    u = 0
    r = 0 # 인구이동이 있는 연합의 개수
    for i in range(N):
        for j in range(N):
            if union[i][j]==0:
                u += 1  # 연합 번호
                r += bfs(u, i, j, N, L, R)
    if r>=1: # 인구이동이 있으면
        cnt += 1
print(cnt)
