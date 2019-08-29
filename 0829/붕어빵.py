T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N 명의 손님, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음.
    t = list(map(int, input().split()))

    sell = [0]*11112 # 시간별 판매량
    for i in t:
        sell[i] += 1
    fish = 0
    for i in range(11112):
        if i>0 and i%M==0: # i시간 재고 계산
            fish += K
        fish -= sell[i] # 시간별로 판매
        if fish<0:
            break

    if fish < 0:
        print('#{} Impossible'.format(tc))
    else:
        print('#{} Possible'.format(tc))
