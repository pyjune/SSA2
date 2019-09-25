dr = [0, -1, 0] # 왼쪽, 위, 오른쪽
dc = [-1, 0, 1]

def shoot(aw, target, N, M, D): # aw가 맞추는 적을 target에 표시
    q = []
    v = [[0]*M for _ in range(N)] #이미 확인한 칸 표시
    q.append(N-1) # 궁수와 거리가 1인 칸은 바로 윗칸
    q.append(aw)
    v[N-1][aw] = 1
    while(len(q)!=0):
        r = q.pop(0)
        c = q.pop(0)

        if target[r][c]>0: # 만약 적이 있이면 가까운 순이므로 적을 맞추고 중지
            target[r][c] += 1
            return
        for k in range(3): # 왼쪽, 앞, 오른쪽 순으로 확인
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<M:
                if v[nr][nc] == 0 and v[r][c]<D: # 아직 확인안한 자리고 사거리 이내면
                    q.append(nr)
                    q.append(nc)
                    v[nr][nc] = v[r][c]+1

def defence(aw1, aw2, aw3, N, M, D):
    target = [[0] * M for _ in range(N)]
    hit = 0
    for i in range(N):
        for j in range(M):
            target[i][j] = enemy[i][j]
    for i in range(N): # 사격 횟수
        # 궁수와 거리가 D이내에서 가장 가까운 적 중 맨 왼쪽의 적을 맞춤
        shoot(aw1, target, N, M, D)
        shoot(aw2, target, N, M, D)
        shoot(aw3, target, N, M, D)
        for r in range(N): # 화살에 맞은 적을 가려냄
            for c in range(M):
                if target[r][c] > 1:
                    hit += 1
                    target[r][c] = 0
        for r in range(N-1, 0, -1):
            for c in range(M):
                target[r][c] = target[r-1][c] # 성벽쪽으로 이동
        for c in range(0, M):
            target[0][c] = 0 # 가장 외곽의 적은 성벽쪽으로 이동하고 없음
    return hit

N, M, D = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in range(M-2): # 맨 왼쪽 궁수
    for j in range(i+1, M-1): # 가운데 궁수
        for k in range(j+1, M): # 오른쪽 궁수
            kill = defence(i, j, k, N, M, D)
            if maxV < kill:
                maxV = kill
print(maxV)
