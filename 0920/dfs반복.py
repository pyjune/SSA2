# 입력
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

#dfs 반복
def dfs(n, V):
    # 초기화
    visited = [0] * (V + 1)  # 방문 표시용
    stack = [0] * V
    top = -1
    # push() + 방문표시
    top += 1
    stack[top] = n
    visited[n] = 1
    while(top>=0): # 스택이 비어있지 않으면
        n = stack[top] # pop()
        top -= 1
        print(n)
        for i in range(1, V+1):
            if adj[n][i]==1 and visited[i]==0:
                top += 1
                stack[top] = i
                visited[i] = 1

V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬 만들기


edge = list(map(int, input().split()))
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1
dfs(1, V)
