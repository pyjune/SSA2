def find(n, k, s):
    global minV
    global used
    global dis
    global p
    if(n==k):
        if(minV>(s+dis[p[n-1]][k])): # 마지막 고객-> 집
           minV = s+dis[p[n-1]][k]
    elif(minV<=s):
        return
    else:
        for i in range(1, N+1):
            if (used[i]==0):
                used[i] = 1
                p[n] = i
                find(n+1, k, s+dis[p[n-1]][p[n]])
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    posin = list(map(int, input().split()))
    posin.append(posin.pop(2)) #회사->고객->집 순으로 저장
    posin.append(posin.pop(2)) #회사->고객->집 순으로 저장

    # 각각의 거리 계산
    dis = [[0]*(N+2) for i in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            dis[i][j] = abs(posin[i*2]-posin[j*2])+abs(posin[i*2+1]-posin[j*2+1])
 
    used = [0]*(N*2)
    used[0] = 1 # 회사는 고정
    p = [0]*(N*2) # 방문순서 저장
    p[0] = 0 # 첫 방문지 회사
    minV = 1000000
    find(1, N+1, 0) # 1번 부터 N+번 집까지
    print('#', end='')
    print(tc, end=' ')
    print(minV)
