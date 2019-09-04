def operate(x):
    dirLetter = 'RDLU'
    target = '#*'
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global tankI
    global tankJ
    global H
    global W
    if x in dirLetter:
        dir = dirLetter.find(x)
        m[tankI][tankJ] = tank[dir]
        ni = tankI + di[dir]
        nj = tankJ + dj[dir]
        if 0<=ni<H and 0<=nj<W and m[ni][nj]=='.':
            m[tankI][tankJ] = '.'
            m[ni][nj] = tank[dir]
            tankI, tankJ = ni, nj
    elif x == 'S':
        tankDir = tank.find(m[tankI][tankJ])
        ni = tankI + di[tankDir]
        nj = tankJ + dj[tankDir]
        while(0<=ni<H and 0<=nj<W):
            if m[ni][nj] == '*' : # 벽돌
                m[ni][nj] = '.' # 폭탄 소멸, 평지화
                return
            elif m[ni][nj] == '#': # 강철
                return # 폭탄 소멸
            ni = ni + di[tankDir]
            nj = nj + dj[tankDir]

tank = '>v<^'

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    m = [list(input()) for _ in range(H)]
    N = int(input())
    cmd = input()
    dir = 0
    tankI = 0
    tankJ = 0
    for i in range (H):
        for j in range(W):
            if m[i][j] in tank:
                tankI = i
                tankJ = j
                dir = tank.find(m[i][j])

    for x in cmd:
        operate(x)
    print('#{}'.format(tc), end = ' ')
    for i in range(H):
        for j in range(W):
            print(m[i][j], end='')
        print()
