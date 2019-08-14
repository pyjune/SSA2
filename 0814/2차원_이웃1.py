
#arr = [list(map(int, input().split())) for i in range(5)]
arr = [[0]*5 for i in range(5)]
k = 1
for i in range(0, 5):
    for j in range(0, 5):
        arr[i][j] = k
        k = k + 1

#모든 칸의 이웃을 출력
for i in range(0, 5):
    for j in range(0, 5):
        if(j+1<=4): # 오른쪽 칸이 존재하면
            print(arr[i][j+1], end=' ')
        if(i+1<=4): # 아래 칸이 존재하면
            print(arr[i+1][j], end=' ')
        if(j-1>=0): # 왼쪽칸이 존재하면
            print(arr[i][j-1], end=' ')
        if(i-1>=0): # 윗칸이 존재하면
            print(arr[i-1][j], end=' ')
        print()
print()
#모든 칸의 이웃 중 짝수만 출력. !반드시 인덱스 범위먼저 검사할 것!
for i in range(0, 5):
    for j in range(0, 5):
        if(j+1<=4 and arr[i][j+1]%2==0 ): # 오른쪽 칸이 존재하면
            print(arr[i][j+1], end=' ')
        if(i+1<=4 and arr[i+1][j]%2==0): # 아래 칸이 존재하면
            print(arr[i+1][j], end=' ')
        if(j-1>=0 and arr[i][j-1]%2==0): # 왼쪽칸이 존재하면
            print(arr[i][j-1], end=' ')
        if(i-1>=0 and arr[i-1][j]%2==0): # 윗칸이 존재하면
            print(arr[i-1][j], end=' ')
        print()
