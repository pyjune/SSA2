# N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int, input().split()))

# 탐색구간 1 : 처리할 원소의 범위
for i in range(1, N):
    #각 원소 Ai에 대해 할일
    minV = arr[0]
    for j in range(1, i): # Ai의 왼쪽 구간에 대해
        if(minV>arr[j]):
            minV = arr[j]
    print(abs(arr[i]-minV), end=' ')
