# 백준 
def f(n, k): # n 사람번호, k 전체인원
    global minV
    if n==k: # 모든 사람의 팀이 결정되면
        s1 = 0 #start의 능력치
        s2 = 0 #link의 능력치
        for i in range(k//2-1):
            for j in range(i+1, k//2):
                s1 += arr[start[i]][start[j]] + arr[start[j]][start[i]]
                s2 += arr[link[i]][link[j]] + arr[link[j]][link[i]]
        if minV>abs(s1-s2):
            minV = abs(s1-s2)
    else:  # 남은 사람이 있으면
        if len(start)<k//2: # start 팀에 남은 자리가 있으면
            start.append(n)
            f(n+1, k)
            start.pop()
        if len(link)<k//2: # link 팀에 남은 자리가 있으면
            link.append(n)
            f(n+1, k)
            link.pop()

N = int(input())
start = []
link = []
minV = 1000000000
arr = [list(map(int, input().split())) for _ in range(N)]
f(0, N)
print(minV)
