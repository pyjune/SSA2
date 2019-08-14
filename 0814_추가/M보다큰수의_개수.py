# N과 M이 주어진다. N개의 정수가 입력될 때 M보다 큰 수의 개수를 출력하시오

# N개의 정수를 입력받아 정수로 리스트에 저장
N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(0, N): #탐색 구간. 0 부터 N개
    if( arr[i] > M): #각 숫자에 대해(리스트의 각 원소에 대해)
        cnt = cnt + 1
print(cnt)
