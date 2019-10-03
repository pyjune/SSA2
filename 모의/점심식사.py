def f(k, pcnt):
    t0 = [0] * 200  # 시간별로 계단을 통과하는 사람 수 기록
    t1 = [0] * 200
    last0 = 0
    last1 = 0
    t0List = [] # 계단에 도착하는 시간 기록
    t1List = []
    for i in range(pcnt):  # i번 사람이 어느 계단으로 갈지 결정
        if k & (1 << i) == 0:  # 0번 계단으로 가는 경우
            t0List.append(dis[i][0])# 0번 계단에 도착하는 시간
        else:
            t1List.append(dis[i][1]) # 1번 계단에 도착하는 시간
    # 시간순으로 정렬
    t0List.sort()
    t1List.sort()

    for tIdx in t0List:
        h = stairs[0][2] # 계단에 머무는 시간
        while(h>0):
            tIdx += 1 # 계단을 내려가기 시작
            if t0[tIdx]<3:
                t0[tIdx] += 1 # tIdx시간에 계단에 머무는 인원 추가
                h -= 1
        last0 = max(last0, tIdx+1)

    for tIdx in t1List:
        h = stairs[1][2]  # 계단에 머무는 시간
        while (h > 0):
            tIdx += 1  # 계단을 내려가기 시작
            if t1[tIdx] < 3:
                t1[tIdx] += 1  # tIdx시간에 계단에 머무는 인원 추가
                h -= 1
        last1 = max(last1, tIdx + 1)
    return max(last0, last1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                person.append([i, j])
            elif m[i][j] != 0:
                stairs.append([i, j, m[i][j]])
    dis = [[0] * 2 for i in range(len(person))]
    for i in range(len(person)):
        dis[i][0] = abs(person[i][0] - stairs[0][0]) + abs(person[i][1] - stairs[0][1])  # 사람i -> 계단0
        dis[i][1] = abs(person[i][0] - stairs[1][0]) + abs(person[i][1] - stairs[1][1])  # 사람i -> 계단0
    minT = 100000000
    for k in range(1 << len(person)):  # 사람이 간 식당을 비트로 표시
        r = f(k, len(person))
        if minT > r:
            minT = r
    print('#{} {}'.format(tc, minT))
