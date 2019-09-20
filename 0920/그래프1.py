def dfs(n, V):
    print(n) # 방문 노드 출력
    visited[n] = 1 # n번 노드에 방문 표시
    for i in range(1, V+1): # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] ==0:  # 인접하고 미방문이면
            dfs(i, V) # i로 이동


V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 만들기
visited = [0]*(V+1) # 방문 표시용
edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    #adj[n2][n1] = 1 # n1에서 n2로 가는 방향성 그래프인 경우 필요없음
dfs(1, V)
