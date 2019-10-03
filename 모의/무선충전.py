
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))
    AP = []
    for i in range(A):
        AP.append(list(map(int, input().split())))
    AP.sort(key=lambda x : x[3], reverse= True) # p가 높은 순으로 정렬

    chargeA = [] # 시간별 충전 영역

    # user 시작 위치
    iA = 1
    jA = 1
    iB = 10
    jB = 10

    sumC = 0
    #  AP와의 거리 계산
    for k in range(M+1): # k초에 대한 충전 확인. 이동은 M회, 출발 점 포함 충전 영역 확인은 M+1회
        wA = []
        wB = []
        for i in range(A):
            if abs(iA-AP[i][1])+abs(jA-AP[i][0])<=AP[i][2]:
                wA.append(i)
            if abs(iB-AP[i][1])+abs(jB-AP[i][0])<=AP[i][2]:
                wB.append(i)
        # A, B가 선택 가능한 모든 경우에 대해 비용을 비교
        maxC = 0
        if len(wA)>0 and len(wB)>0: # A, B 모두 충전영역에 있는 경우
            for x in wA:
                for y in wB:
                    if x==y: # 같은 충전기인 경우
                        if maxC<AP[x][3]:
                            maxC = AP[x][3]
                    else: # 다른 충전기인 경우
                        if maxC<AP[x][3]+AP[y][3]:
                            maxC = AP[x][3]+AP[y][3]
        elif len(wA)>0: # A만 충전영역에 있는 경우
            for x in wA:
                if maxC<AP[x][3]:
                    maxC = AP[x][3]
        elif len(wB)>0: # B만 충전영역에 있는 경우
            for y in wB:
                if maxC<AP[y][3]:
                    maxC = AP[y][3]
        sumC += maxC

        if k<M: # 이동횟수가 남은 경우
            iA = iA+di[userA[k]]
            jA = jA+dj[userA[k]]
            iB = iB+di[userB[k]]
            jB = jB+dj[userB[k]]

    print('#{} {}'.format(tc, sumC))
