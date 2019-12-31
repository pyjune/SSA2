dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
left = [3, 0, 1, 2]

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(N)]
clean = 1 # 청소한 칸 수
arr[r][c] = 2 # 청소한 칸
while True:
    cnt = 0
    while arr[r+dr[left[d]]][c+dc[left[d]]] != 0: # 진행방향의 왼쪽이 청소할 칸이 아니면
        cnt += 1 # 방향전환 횟수를 기록하고
        d = left[d]  # 왼쪽으로 방향 전환
        if cnt==4: # 4방향 모두 청소할 칸이 아니면
            break

    if cnt<4: #청소할 칸이면
        clean += 1
        d = left[d]
        r += dr[d]
        c += dc[d]
        arr[r][c] = 2 # 청소
    else: # 모든 방향에 청소할 칸이 없으면 1칸 후진
        if arr[r-dr[d]][c-dc[d]]!=1 :
            r -= dr[d]
            c -= dc[d]
        else:
            break
print(clean)
