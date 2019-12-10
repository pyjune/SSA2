di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def f(i, j, N):
    global homecnt
    v[i][j] = 1 # 방문표시
    homecnt += 1
    #if j+1<N and arr[i][j+1]=='1' and v[i][j+1]==0 :
    #    f(i, j+1, N) # 각 방향별로 확인하는 경우
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]=='1' and v[ni][nj]==0:
                f(ni, nj, N)

N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)] # 단지에 이미 포함된 위치 표시
home = []

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and v[i][j]==0: # 단지에 속하지 않은 건물을 찾으면
            homecnt = 0 # 단지 내부 건물 수 카운트
            f(i, j, N)
            cnt += 1 # 단지의 수
            home.append(homecnt)
home.sort()
print(cnt)
for x in home:
    print(x)
