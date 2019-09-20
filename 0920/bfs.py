def bfs(n, V):
    q = [0]*V # 큐 생성
    f = -1
    r = -1
    visited = [0]*(V+1) # 방문표시 배열
    # 시작점 인큐 + 방문표시
    r += 1
    q[r] = n
    visited[n] = 1
    while(f != r): # 큐가 비어있지 않으면 반복
        f += 1 # 디큐
        n = q[f]
        print(n)
        # n에 인접하고 미방문인 노드 i를 인큐 + 방문표시
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0:
                r += 1
                q[r] = i
                visited[i] = 1



V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 만들기

edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

bfs(1, V)
