def find(n, k, c):
    global maxV
    global minC
    if(c==0 or n==k):
        s = 0
        for i in range(k):
            s = s*10 + int(card[i])
        if(maxV <= s):
            maxV = s
            if(minC>c):
                minC = c
    else:
        lst = list(str(card))
        for i in range(k):
            card[n], card[i] = card[i], card[n]
            cnt = 1 if n!=i else 0
            find(n+1, k, c-cnt)
            card[n], card[i] = card[i], card[n]

T = int(input())
for tc in range(1, T+1):
    c, N = input().split()
    card = list(c)
    maxV = 0
    minC = int(N)
    for i in range(len(card)):
        maxV = maxV*10 + int(card[i])
    find(0, len(card), int(N))
    if(minC%2 != 0):
        n1 = maxV%10
        n2 = maxV%100//10
        maxV = maxV//100*100+n1*10+n2
    print('#{} {}'.format(tc, maxV))
