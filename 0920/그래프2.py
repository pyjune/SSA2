# 입력
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(n, V):
    print(n) # 방문 노드 출력
    visited[n] = 1 # n번 노드에 방문 표시
    for i in range(1, V+1): # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] ==0:  # 인접하고 미방문이면
            dfs(i, V) # i로 이동

def dfs2(n, k, V): # 찾는 노드에 도착하면 탐색 중지
    if n==k: # 찾는 노드에 도착한 경우
        return 1 # 목적지를 찾아서 중단하는 경우
    else:
        visited[n] = 1 # n번 노드에 방문 표시
        for i in range(1, V+1): # 모든 노드 i에 대해
            if adj[n][i] == 1 and visited[i] ==0:  # 인접하고 미방문이면
                if dfs2(i, k, V)==1: # i로 이동, 목적지를 찾은 경우
                    return 1 # 다른 갈림길을 찾지 않고 중단
        return 0 # 현재 노드 이후로 목적지가 없는 경우

V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 만들기
visited = [0]*(V+1) # 방문 표시용
edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    #adj[n2][n1] = 1 # n1에서 n2로 가는 방향성 그래프인 경우 필요없음
#dfs(4, V)
print(dfs2(1, 7, V)) # 1에서 7로 가는 경로가 있으면 1, 없으면 0을 출력

