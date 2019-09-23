#입력
7 4  			# V E, V 1~V번 노드가 있고, E개의 간선 정보가 주어짐
2 3 4 5 4 6 7 6
3 6 			# 두 노드가 같은 트리에 속하는지 확인


def rep(n):
    while(p[n]!=n):
        n = p[n]
    return n

V, E = map(int, input().split())
edge = list(map(int, input().split()))
v1, v2 = map(int, input().split())
p = [i for i in range(V+1)]
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    p[rep(n2)] = rep(n1) # union(n1, n2) 인 경우(n1이 대표 원소)
    #p[rep(n1)] = rep(n2) # union(n2, n1)

# 트리의 수 구하기 (상호배타집합의 개수)
cnt = 0
for i in range(1, V+1):
    if p[i]==i: # 인덱스와 대표원소가 같으면 대표원소
        cnt += 1
# 같은 트리에 속하는가?
r = 1 if rep(v1)==rep(v2) else 0
print(cnt, r)
