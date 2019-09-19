def f(i, N):
    global cnt
    if i==N:
        cnt += 1
    else:
        for j in range(N):
            if col[j]==0 and diag1[i+N-1-j]==0 and diag2[i+j]==0:
                col[j] = 1
                diag1[i + N - 1 - j] =1
                diag2[i + j] =1
                f(i+1, N)
                col[j] = 0
                diag1[i + N - 1 - j] = 0
                diag2[i + j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    col = [0]*N
    diag1 = [0]*2*N
    diag2 = [0]*2*N
    f(0, N)
    print('#{} {}'.format(tc, cnt))
    
---------------------------------------------------
# 추가 설명
f(i, N)
	if i==N # 모든 줄에 퀸을 놓으면
		cnt += 1
	else
		for j : 0->N-1
			if col[j]==0 and right[i+j]==0 and left[i-j+N-1]==0 
				# 다른 줄에 j번 열에 퀸이 없어야 하고
				# 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
				#board[i][j] = 1
				col[j] = 1 # 현재 줄에서 j열을 사용함으로 표시
				right[i+j]= 1
				left[i-j+N-1]= 1
				f(i+1, N) # j열에 놓을 수 있으면 다음 줄로 이동
				col[j] = 0
				right[i+j]= 0
				left[i-j+N-1]= 0
				#board[i][j] = 0

f(0, N)    
