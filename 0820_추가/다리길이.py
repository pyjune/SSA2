# 봉우리의 개수와 다리 길이
N = int(input())
arr = list(map(int, input().split()))

slope = 0 # 0 내리막 1 오르막
cnt = 0
size = 0
maxV = 0
for i in range(1, N):
    if arr[i-1] > arr[i]:
        if slope == 1: #내리막이고 이전까지 오르막이면
            cnt += 1    # 오르막->내리막인 봉우리 이므로
            slope = 0

            if maxV <size:
                maxV = size
            size = 1
    else:
        slope = 1
    if size>0:
        size += 1
if cnt<2:
    maxV = 0
print(cnt, maxV)
