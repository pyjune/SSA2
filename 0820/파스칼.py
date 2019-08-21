T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    #print('#{}'.format(tc)) # 값의 결정과 동시에 출력하는 경우
    for i in range(N):
        for j in range(i+1):
            if j==0 or i==j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            #print(arr[i][j], end=' ') # 값의 결정과 동시에 출력하는 경우
        #print() # 값의 결정과 동시에 출력하는 경우

    # 테이블 완성 후 출력하는 경우
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()
