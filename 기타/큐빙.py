def f(i, j, d): # 회전 기준면
    if d=='+': # CW
        t1, t2 = cube[i][j+2], cube[i][j+1]
        cube[i][j+2], cube[i][j + 1] = cube[i][j], cube[i+1][j]
        cube[i][j], cube[i + 1][j] = cube[i+2][j], cube[i+2][j+1]
        cube[i + 2][j], cube[i + 2][j + 1] = cube[i+2][j+2], cube[i+1][j+2]
        cube[i + 2][j + 2], cube[i + 1][j + 2] = t1, t2
    else: # CCW
        t1, t2 = cube[i][j], cube[i][j + 1]
        cube[i][j], cube[i][j + 1] = cube[i][j+2], cube[i+1][j+2]
        cube[i][j + 2], cube[i + 1][j + 2] = cube[i+2][j+2], cube[i+2][j+1]
        cube[i + 2][j + 2], cube[i + 2][j + 1] = cube[i+2][j], cube[i+1][j]
        cube[i + 2][j], cube[i + 1][j] = t1, t2

def ud(x):
    diff = 0 if x[0]=='U' else 2
    if x=='U+' or x=='D-': # CW
        t1, t2, t3 = cube[2-diff][3], cube[2-diff][4], cube[2-diff][5]
        cube[2-diff][3], cube[2-diff][4], cube[2-diff][5] = cube[5][2-diff], cube[4][2-diff], cube[3][2-diff]
        cube[5][2-diff], cube[4][2-diff], cube[3][2-diff] = cube[6+diff][5], cube[6+diff][4], cube[6+diff][3]
        cube[6+diff][5], cube[6+diff][4], cube[6+diff][3] = cube[3][6+diff], cube[4][6+diff], cube[5][6+diff]
        cube[3][6+diff], cube[4][6+diff], cube[5][6+diff] = t1, t2, t3
        if x=='U+':
            f(3, 3, '+')
        else:
            f(9, 3, '-')
    elif x=='U-' or x=='D+': # CCW
        t1, t2, t3 = cube[2-diff][3], cube[2-diff][4], cube[2-diff][5]
        cube[2-diff][3], cube[2-diff][4], cube[2-diff][5] = cube[3][6+diff], cube[4][6+diff], cube[5][6+diff]
        cube[3][6+diff], cube[4][6+diff], cube[5][6+diff] = cube[6+diff][5], cube[6+diff][4], cube[6+diff][3]
        cube[6+diff][5], cube[6+diff][4], cube[6+diff][3] = cube[5][2-diff], cube[4][2-diff], cube[3][2-diff]
        cube[5][2-diff], cube[4][2-diff], cube[3][2-diff] = t1, t2, t3
        if x=='U-':
            f(3, 3, '-')
        else:
            f(9, 3, '+')

def fb(x):
    diff = 0 if x[0] == 'F' else 2
    if x=='F+' or x=='B-':
        t1, t2, t3 = cube[9+diff][3],cube[9+diff][4],cube[9+diff][5]
        cube[9 + diff][3], cube[9 + diff][4], cube[9 + diff][5] = cube[5-diff][8], cube[5-diff][7], cube[5-diff][6]
        cube[5 - diff][8], cube[5 - diff][7], cube[5 - diff][6] = cube[5-diff][5], cube[5-diff][4], cube[5-diff][3]
        cube[5 - diff][5], cube[5 - diff][4], cube[5 - diff][3] = cube[5-diff][2], cube[5-diff][1], cube[5-diff][0]
        cube[5 - diff][2], cube[5 - diff][1], cube[5 - diff][0] = t1, t2, t3
        if x=='F+':
            f(6, 3, '+')
        else:
            f(0,3, '-')
    if x=='F-' or x=='B+':
        t1, t2, t3 = cube[9+diff][5],cube[9+diff][4],cube[9+diff][3]
        cube[9 + diff][5], cube[9 + diff][4], cube[9 + diff][3] = cube[5-diff][0], cube[5-diff][1], cube[5-diff][2]
        cube[5 - diff][0], cube[5 - diff][1], cube[5 - diff][2] = cube[5-diff][3], cube[5-diff][4], cube[5-diff][5]
        cube[5 - diff][3], cube[5 - diff][4], cube[5 - diff][5] = cube[5-diff][6], cube[5-diff][7], cube[5-diff][8]
        cube[5 - diff][6], cube[5 - diff][7], cube[5 - diff][8] = t1, t2, t3
        if x=='F-':
            f(6, 3, '-')
        else:
            f(0, 3, '+')
def lr(x):
    diff = 0 if x[0] == 'L' else 2
    if x=='L+' or x=='R-':
        t1, t2, t3 = cube[11][3+diff], cube[10][3+diff], cube[9][3+diff]
        cube[11][3 + diff], cube[10][3 + diff], cube[9][3 + diff] = cube[8][3+diff], cube[7][3+diff], cube[6][3+diff]
        cube[8][3 + diff], cube[7][3 + diff], cube[6][3 + diff] = cube[5][3+diff], cube[4][3+diff], cube[3][3+diff]
        cube[5][3 + diff], cube[4][3 + diff], cube[3][3 + diff] = cube[2][3+diff], cube[1][3+diff], cube[0][3+diff]
        cube[2][3 + diff], cube[1][3 + diff], cube[0][3 + diff] = t1, t2, t3
        if x=='L+':
            f(3, 0, '+')
        else:
            f(3, 6, '-')
    elif x=='L-' or x=='R+':
        t1, t2, t3 = cube[9][3+diff], cube[10][3+diff], cube[11][3+diff]
        cube[9][3 + diff], cube[10][3 + diff], cube[11][3 + diff] = cube[0][3+diff], cube[1][3+diff], cube[2][3+diff]
        cube[0][3 + diff], cube[1][3 + diff], cube[2][3 + diff] = cube[3][3+diff], cube[4][3+diff], cube[5][3+diff]
        cube[3][3 + diff], cube[4][3 + diff], cube[5][3 + diff] = cube[6][3+diff], cube[7][3+diff], cube[8][3+diff]
        cube[6][3 + diff], cube[7][3 + diff], cube[8][3 + diff] = t1, t2, t3
        if x=='L-':
            f(3, 0, '-')
        else:
            f(3, 6, '+')

T = int(input())
for tc in range(T):
    cube = [['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x'],
            ]
    n = int(input())
    cmd = list(input().split())
    for x in cmd:
        if x[0]=='U' or x[0]=='D':
            ud(x)
        elif x[0]=='L' or x[0]=='R':
            lr(x)
        elif x[0]=='F' or x[0]=='B':
            fb(x)
    for i in range(3, 6):
        for j in range(3, 6):
            print(cube[i][j], end='')
        print()
