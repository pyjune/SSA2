def f(i, N, r, s): # i 현재 날짜순서, N 총 근무일, r 진행중인 상담의 남은 날짜, s 현재까지의 이익
    global maxV
    if i==N:
        if maxV<s:
            maxV = s
    else:
        if r==0 and T[i]+i<=N:
            f(i+1, N, T[i]-1, s+P[i]) # i상담 시작
        if r-1<0:
            r=1
        f(i+1, N, r-1, s)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())
maxV = 0
f(0, N, 0, 0)
print(maxV)
