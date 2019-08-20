def f(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maze
    global N
    #if maze[i][j] == '1':
    #    return 0
    if maze[i][j] == '3': #목적지면
        return 1
    else:
        maze[i][j] = '1' #방문 표시. 벽으로 바꿈
        #이동할 좌표 생성
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:
                if maze[ni][nj] != '1': #  벽이 아니면 방문
                    if f(ni, nj)==1: # 진행방향에서 목적지를 찾은 경우
                        return 1
        return 0 # 현재위치에서 갈 수 있는 방향에서 목적지를 찾지 못함. 이전의 다른 방향 탐색

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}'.format(tc, f(startI, startJ)))
