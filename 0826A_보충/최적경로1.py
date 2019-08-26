def npr(n, k, m):
    global used
    global p
    global dis
    global minV
    if n==k:
        s = dis[0][p[0]] # 회사 - 첫번째 고객
        for i in range(1, k):
            s += dis[p[i-1]][p[i]] # 고객사이 이동 거리
        s += dis[p[k-1]][1] # 마지막 고객 - 집 거리
        if minV>s:
            minV = s
    else:
        for i in range(m):
            if used[i]==0:
                used[i] = 1
                p[n] = i+2 # 고객번호
                npr(n+1, k, m)
                used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    used = [0]*N
    p = [0]*N
    dis = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            dis[i][j] = abs(arr[i*2]-arr[j*2])+abs(arr[i*2+1]-arr[j*2+1])

    minV = 10000
    npr(0, N, N)
    print(minV)

