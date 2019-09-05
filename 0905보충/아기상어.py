def f(N, size):
    global fishI
    global fishJ
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    minV = 0
    q = []
    visited = [[0]*N for _ in range(N)]
    checked = [[0]*N for _ in range(N)]
    q.append(fishI)
    q.append(fishJ)
    visited[fishI][fishJ] = 1
    while(len(q)!=0):
        i = q.pop(0)
        j = q.pop(0)
        if checked[i][j] == 0 and 0<sea[i][j]<size: # 확인 안된 작은 물고기가 있을 때
            if minV == 0: # 처음 만나는 물고기인 경우 거리 저장
                minV = visited[i][j]
                checked[i][j] = minV
            elif visited[i][j] == minV: # 가장 가까운 물고기와 같은 거리면
                checked[i][j] = minV
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if sea[ni][nj]<=size and visited[ni][nj]==0:
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = visited[i][j] + 1

    for i in range(N):
        for j in range(N):
            if checked[i][j] != 0:
                fishI = i # 물고기를 잡아먹은 새로운 상어 위치
                fishJ = j
                sea[i][j] = 0
                return checked[i][j]-1
    return 0


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

size = 2
fishI = 0
fishJ = 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            fishI = i
            fishJ = j
            sea[i][j] = 0
r = 1
sec = 0
eatCnt = 0
while(r!=0):
    r = f(N, size) # 물고기를 먹는데 걸린 시간 리턴
    sec += r
    if r!=0: # 물고기를 먹었으면
        eatCnt += 1
        if eatCnt == size: # 몸집만큼 먹었으면
            size += 1   # 상어가 1 커지고
            eatCnt = 0  # 먹은 물고기 수 초기화
print(sec) # 가능한 물고기를 잡아먹는데 걸린 시간
