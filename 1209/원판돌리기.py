di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, T = map(int, input().split())
arr1 = [[0]*M] + [list(map(int, input().split())) for _ in range(N)] + [[0]*M] # 0번과 N+1을 더미로 붙임
org = arr1
arr2 = [[0] * M for _ in range(N + 2)]
dest = arr2
for tc in range(T):
    x, d, k = map(int, input().split())
    for i in range(1, N+1): # 모든 원판에 대해
        if i%x==0: # x의 배수면
            if d: # 반시계 방향
                for j in range(k): # k번 회전
                    v = org[i].pop(0)
                    org[i].append(v)
            else: # 시계 방향
                for j in range(k):
                    v = org[i].pop()
                    org[i].insert(0, v)

    check = False # 인접에 같은 숫자가 있는지 기록할 변수

    for i in range(1, N+1):
        for j in range(M):
            dest[i][j] = org[i][j] # 인접을 지울 복사본 만들기
    s = [] # 평균을 구할 숫자 목록
    for i in range(1, N+1): # 인접의 같은 수 찾기 => 회전 결과에 대해 bfs로 찾는것도 가능
        for j in range(0, M):
             for k in range(4):
                 if org[i][j]!=0 and org[i][j]==org[i+di[k]][(j+dj[k])%M]: # -1은 마지막 원소로, M은 0으로
                    dest[i+di[k]][(j+dj[k])%M] = 0
                    dest[i][j] = 0
                    check = True # 인접에 같은 숫자 있음
             if dest[i][j]!=0: # 인접에 같은 값이 없는 숫자 목록
                s.append(dest[i][j])
    if check==False and len(s)!=0: # 같은 숫자가 없는 경우. 단, 전부 0인 경우 제외
        avg = sum(s)/len(s) # 평균구하기
        for i in range(1, N+1):
            for j in range(M):
                if dest[i][j]!=0:
                    if dest[i][j]>avg: # 평균보다 크면 1 빼고
                        dest[i][j]-=1
                    elif dest[i][j]<avg: # 작으면 1 더함
                        dest[i][j]+=1
    org, dest = dest, org # 결과를 다시 원본으로
total = 0
for i in range(1, N+1):
    for j in range(M):
        total += org[i][j]
print(total)
