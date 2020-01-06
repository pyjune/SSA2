dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

grid = [[0]*101 for _ in range(101)]
N = int(input())
for k in range(N):
    x, y, d, g = map(int, input().split())
    direction = [0]*(2**g) # 각 세대에 대한 모든 방향 저장
    direction[0] = d
    grid[y][x] = 1 # 0세대 시작
    y += dy[d]
    x += dx[d]
    grid[y][x] = 1 # 0세대 끝==1세대 시작
    for n in range (1, g+1): # g 세대까지 반복
        i = 2**(n-1) # diection에서 n세대 시작 인덱스
        for j in range(i): # 기준 인덱스 이전 모든 구간 만큼
            direction[i+j] = (direction[i-j-1] + 1)%4 # 현재 위치로 이동하기 위한 방향
            y += dy[direction[i + j]] 
            x += dx[direction[i + j]]
            grid[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        s = grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]
        if s==4:
            cnt += 1
print(cnt)
