# 백준 3190 참고
def f(N, L):
    tail = [] #꼬리의 위치
    r, c, d = 1, 1, 0 # 출발 위치, 방향
    tail.append((r, c))
    arr[r][c] = 1 # 이동 방향 저장
    t = 0 # 진행시간
    cnt = 0 #방향전환 횟수
    while True:
        t += 1 # 1초 경과
        r += dr[d] # 다음 칸
        c += dc[d]
        if 1<=r<=N and 1<=c<=N:
            if arr[r][c]==1: # 몸통에 닿으면
                break
            else:
                if arr[r][c]!=10: #사과가 아니면
                    rr, cc = tail.pop(0)
                    arr[rr][cc] = 0 # 꼬리 이동
                tail.append((r, c)) # 머리 추가
                arr[r][c] = 1 # 머리 위치
                if cnt<L and t==cmd[cnt][0]: # 방향 전환
                    d = toL[d] if cmd[cnt][1]=='L' else toD[d]
                    cnt += 1
        else: # 벽에 닿으면
            break
    return t

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
toL = [3, 0, 1, 2]
toD = [1, 2, 3, 0]

N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)] # 좌표가 1부터 
K = int(input())
for i in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 10 # 사과가 있는 자리
L = int(input())
cmd = []
for i in range(L):
    t, ld = input().split()
    cmd.append((int(t), ld))
print(f(N, L))
