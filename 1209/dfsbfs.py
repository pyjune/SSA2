# 백준 1260 DFS와 BFS

def dfs(v, N):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N+1): # 모든 노드 i에 대해
        if adj[v][i]==1 and visited[i]==0: #  v와 인접하고 방문안한 노드면 이동
            dfs(i, N)

def bfs(n, V): #  bfs(n, k, V) , k번 노드에 도착하는지 확인하는 탐색
    q = []
    q.append(n) # 시작노드 인큐
    visited[n] = 1 # 인큐한 노드 표시

    while q: # 큐에 노드가 남아있으면 반복
        n = q.pop(0) # 디큐 (처리할 노드 꺼냄)
        print(n, end=' ') # 노드번호 출력
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0: #n에 인접하고 처리안한 노드면
                q.append(i)
                visited[i] = visited[n] + 1 # 방문표시와 거리정보를 동시 저장

N, M, V = map(int, input().split()) # 노드수, 간선수, 시작노드
adj = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

dfs(V, N)
print()
visited = [0]*(N+1)
bfs(V, N)
