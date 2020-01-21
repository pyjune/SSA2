def mv(i,C): # i 가상 인덱스, C 크기
    if i<=0:
        b = 1 - i # 잘라 붙일 총 칸 수
        e = ((b-1)//(C-1))%2 # 조각 번호
        if e==0: # 짝수면 ->
            i = 2+(b-1)%(C-1)
        else: # 홀수면
            i = C-1-(b-1)%(C-1)
        return i, e
    elif i>C:
        b = i - C
        e = ((b-1)//(C-1))%2
        if e==0: # 짝수면
            i = C-1-(b-1)%(C-1)
        else:
            i = 2+(b-1)%(C-1)
        return i, e

# 방향 1 위 2 아래 3 오른쪽 4 왼쪽
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
R, C, M = map(int, input().split())
sea = [[0]*(C+1) for _ in range(R+1)]
shark = [[0]]
for i in range(1, M+1): # 상어 번호 표시
    r, c, s, d, z = map(int, input().split())
    sea[r][c] = i
    shark.append([s, d, z]) # 상업 번호별로 속력, 방향, 크기 저장
get = 0 # 잡은 상어 크기의 합
for f in range(1, C+1): # 낚시왕의 위치
    for i in range(1, R+1):
        if sea[i][f]!=0: # 상어가 있으면
            get += shark[sea[i][f]][2] # 가장 가까운 상어를 잡아 크기를 더하고
            sea[i][f] = 0
            break # 상어 이동
    dest = [[0]*(C+1) for _ in range(R+1)] # 상어가 이동한 결과를 저장할 배열
    for i in range(1, R+1):
        for j in range(1, C+1):
            if sea[i][j]!=0: # 상어가 있으면
                t = sea[i][j] # 상어번호
                s = shark[t][0]  # 속력
                d = shark[t][1] # 방향
                z = shark[t][2] # 크기
                ni = i + di[d]*s
                nj = j + dj[d]*s
                if ni<=0: # d==1 위쪽인 경우
                    ni, e = mv(ni, R) # e 조각번호 홀/짝수
                    if e==0: # 짝수면 반대
                        d = 2
                elif ni>R: # d==2 아래쪽인 경우
                    ni, e = mv(ni, R)
                    if e==0: # 짝수면 반대
                        d = 1
                elif nj<=0: # d==4 왼쪽인 경우:
                    nj, e = mv(nj, C)
                    if e==0: # 짝수면 반대
                        d = 3
                elif nj>C: # d==3 오른쪽인 경우
                    nj, e = mv(nj, C)
                    if e==0: # 짝수면 반대
                        d = 4
                shark[t][1] = d # 방향 수정
                if dest[ni][nj]!=0: # 다른 물고기가 있으면
                    if shark[dest[ni][nj]][2]<z: # 크기 비교, 더 크면
                        dest[ni][nj] = t # 잡아먹음
                else:
                    dest[ni][nj] = t
    sea = dest # 이동한 결과에서 다시 반복
print(get)
