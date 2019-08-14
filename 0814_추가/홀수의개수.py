# N과 N개의 정수가 한 줄에 입력된다. N개의 정수 중 홀수의 개수를 출력하시오.
# 8 7 2 4 3 6 2 4 5

# N개의 정수를 입력받아 정수로 리스트에 저장

arr = list(map(int, input().split()))
N = arr[0]
cnt = 0
#for i in range(1, arr[0]+1):#탐색구간
for i in range(1, N+1):#탐색구간
    if(arr[i] % 2 == 1):
        cnt = cnt + 1        
print(cnt)
