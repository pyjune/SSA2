# 봉우리의 개수
N = int(input())
arr = list(map(int, input().split()))

slope = 0 # 0 내리막 1 오르막
cnt = 0
for i in range(1, N):
    if arr[i-1] > arr[i]:
        if slope == 1: #내리막이고 이전까지 오르막이면
            cnt += 1    # 오르막->내리막인 봉우리 이므로
            slope = 0
    else:
        slope = 1

print(cnt)
