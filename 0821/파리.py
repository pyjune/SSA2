T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    for i in range(0, N-K+1): # 부분 영역의 왼쪽 위 모서리칸 좌표, i, j
        for j in range(0, N-K+1):
            s = 0 # 부분 영역의 합
            for r in range(i, i+K): # 영역내부의 행 번호 i~i+K-1
                for c in range(j, j+K): # 영역 내부의 열 번호
                    s += fly[r][c] 
            if maxV<s:
                maxV = s
    print('#{} {}'.format(tc, maxV))
