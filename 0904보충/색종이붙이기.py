def f(n, s): # n 사용한 종이수, s 남은 1
    global minV
    if s==0:
        if minV>n:
            minV = n
    elif n>=minV:
        return
    #elif minV==4:
     #   return
    elif sum(paper)==0:
        return
    else:
        for i in range(10):
            for j in range(10):
                if m[i][j]==1 and visited[i][j] ==0: # 왼쪽 모서리로 가정
                    for k in range(5, 0, -1): # 덮는 크기

                        if paper[k]>0 and i+k<=10 and j+k<=10: # 종이가 남아있고
                            cover = 0
                            for r in range(i, i+k):
                                for c in range(j, j+k):
                                    if visited[r][c]==0:
                                        cover += m[r][c]
                            if cover==(k*k): # 덮어지면
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 1
                                paper[k] -= 1
                                f(n+1, s-k*k)
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 0
                                paper[k] += 1
                    return

m = [list(map(int, input().split()))for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
minV = 26
s = 0
paper = [0, 5, 5, 5, 5, 5]
for i in range(10):
    for j in range(10):
        if m[i][j]==1:
            s += 1
f(0, s)
if minV == 26:
    minV = -1
print(minV)
