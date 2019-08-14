# 바로 왼쪽의 숫자보다 큰 숫자의 개수는?
# N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int, input().split()))

cnt = 0
# 탐색구간
for i in range(1, N):
    if(arr[i-1]<arr[i]):
       cnt = cnt + 1
print(cnt)
