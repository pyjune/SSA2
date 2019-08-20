# 증가구간의 최대 길이
N = int(input())
arr = list(map(int, input().split()))

maxV = 1
size = 1
for i in range(1, N):
    if arr[i-1]<arr[i]: # 증가 구간인 경우
        size += 1 # 이전 까지의 증가구간 길이 + 1
        if maxV < size:
            maxV = size
    else: #증가구간이 아니면 증가구간의 길이를 1로 
        size = 1
print(maxV)
