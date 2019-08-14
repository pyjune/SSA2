# N개의 정수를 입력받아 정수로 리스트에 저장
N = int(input())
arr = list(map(int, input().split()))

cnt = 0 # 짝수의 개수 기록
for i in range(0, N): #탐색 구간. 0 부터 N개
    if(arr[i] % 2 == 0): #각 숫자에 대해(리스트의 각 원소에 대해)
        cnt = cnt + 1
print(cnt)
