N, K = map(int, input().split())
arr = list(map(int, input().split()))

i = 0 # 탐색을 시작하는 위치
cntK = 0
while(i<N):
    while(i<N and arr[i]==0): # 0인 구간을 통과. arr[i]==1인 위치에서 빠져나옴
        i += 1
    cnt = 0
    while(i<N and arr[i]==1): # 1인 구간을 이동. 1의 개수 카운트
        cnt += 1
        i += 1
    if cnt==K:
        cntK += 1
print(cntK)
