# 백준 17144

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(R): # 공기청정기 위치 기록
    if A[i][0]==-1:
        cleaner.append(i) 
org = A # 확산 전
for _ in range(T):
    dest = [[0]*C for _ in range(R)] # 확산 후 결과 저장
    for i in range(R):
        for j in range(C):
            if org[i][j]>0: # 미세먼지가 있으면 확산
                diffuse = []
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<R and 0<=nj<C and org[ni][nj]!=-1:
                        diffuse.append((ni, nj))
                v = org[i][j]//5
                for x in diffuse:
                    dest[x[0]][x[1]] += v
                dest[i][j] += org[i][j]-v*len(diffuse)
    # 공기순환
    for i in range(cleaner[0]-1, 0, -1): # 청정기 윗칸까지
        dest[i][0] = dest[i-1][0]
    for i in range(0, C-1):
        dest[0][i] = dest[0][i+1]
    for i in range(0, cleaner[0]):
        dest[i][C-1] = dest[i+1][C-1]
    for i in range(C-1, 0, -1):
        dest[cleaner[0]][i] = dest[cleaner[0]][i-1]

    for i in range(cleaner[1]+1, R-1):
        dest[i][0] = dest[i+1][0]
    for i in range(0, C-1):
        dest[R-1][i] = dest[R-1][i+1]
    for i in range(R-1, cleaner[1], -1):
        dest[i][C-1] = dest[i-1][C-1]
    for i in range(C-1, 0, -1):
        dest[cleaner[1]][i] = dest[cleaner[1]][i-1]

    org = dest # 확산 및 청정 결과물을 다시 원본으로
    org[cleaner[0]][0] = -1 # 확산시 청정기 정보가 없어지므로 다시 기록
    org[cleaner[1]][0] = -1

s = 0
for i in range(R): # 먼지 농도 합계
    s += sum(org[i])
print(s+2) # 공기 청정기 (-1 * 2) 만큼 더함
