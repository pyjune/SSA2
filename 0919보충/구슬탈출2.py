di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# n 기울인 횟수
# c 빠져나온 구슬 정보   R 1, B 2, R+B 3

def f(n, iR, jR, iB, jB, c, dir):
    global minV
    if c==1: # 빨간공만 빠져 나온 경우
        if minV>n:
            minV = n
    elif c>1: # 파란공이 빠져 나오거나 둘 다 나온 경우
        return
    elif n==10: # 10번을 움직인 경우
        return
    else: # 각 방향으로 기울이기
        for k in range(4):
            p = [iR, jR, iB, jB]
            if dir==-1 or (k!= dir and k!=(dir+2)%4): # 이전 방향이나 반대 방향이 아닌 경우
                c, p = move(p, k) # 구슬 이동
                if c==0 and iR==p[0] and jR==p[1] and iB==p[2] and jB==p[3]: # 구슬이 움직이지 않은 경우
                    continue
                else:
                    f(n+1, p[0], p[1], p[2], p[3], c, k)

def move(p, d):
    niR, njR = p[0], p[1]
    niB, njB = p[2], p[3]
    cnt = 0
    while(bd[niR+di[d]][njR+dj[d]]!='#' and bd[niR+di[d]][njR+dj[d]]!='O'):
        niR, njR = niR+di[d], njR+dj[d]
    if bd[niR+di[d]][njR+dj[d]]=='O':
        cnt += 1
    while(bd[niB+di[d]][njB+dj[d]]!='#' and bd[niB+di[d]][njB+dj[d]]!='O'):
        niB, njB = niB+di[d], njB+dj[d]
    if bd[niB+di[d]][njB+dj[d]]=='O':
        cnt += 2

    if cnt>0:

        return cnt, p # 빠져나간 구슬 갯수 리턴
    #구슬이 겹치면 원래 순서 유지

    if niR==niB and njR==njB:
        if d == 0: # 오른쪽인 경우, column 비교
            t1 = njR - 1 if p[1]<p[3] else njR # B가 오른쪽이면
            t3 = njB if p[1]<p[3] else njB-1
            p = [niR, t1, niB, t3]
        elif d == 1: # 아래쪽인 경우, row 비교
            t0 = niR -1 if p[0]<p[2] else niR # B가 아래면
            t2 = niB if p[0]<p[2] else niB -1
            p = [t0, njR, t2, njB]
        elif d == 2: # 왼쪽인 경우 column 비교
            t1 = njR if p[1] < p[3] else njR + 1  # B가 오른쪽이면
            t3 = njB+1 if p[1] < p[3] else njB
            p = [niR, t1, niB, t3]
        elif d == 3: # 위쪽인 경우, row 비교
            t0 = niR if p[0]<p[2] else niR +1# B가 아래면
            t2 = niB+1 if p[0]<p[2] else niB
            p = [t0, njR, t2, njB]
    else:
        p = [niR, njR, niB, njB]
    return cnt, p

N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]
R = []
B = []
for i in range(N):
    for j in range(M):
        if bd[i][j]=='R':
            R.append(i)
            R.append(j)
            bd[i][j] = '.'
        if bd[i][j]=='B':
            B.append(i)
            B.append(j)
            bd[i][j] == '.'
minV = 11
f(0, R[0], R[1], B[0], B[1], 0, -1)
if minV == 11:
    minV = -1
print(minV)
