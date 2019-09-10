def enq(n):
    global last
    # 완전이진트리 유지
    last += 1 # 마지막 노드를 추가하고
    heap[last] = n # 마지막 노드에 데이터 저장
    # 최소힙 유지 ( 부모 노드의 데이터가 더 작음)
    c = last
    while(c//2>0 and heap[c//2]>heap[c]): # 부모가 있고, 부모 노드의 데이터가 더 크면 교환
        heap[c // 2], heap[c] = heap[c], heap[c//2]
        c = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)
    num = list(map(int,input().split()))
    last = 0
    for x in num:
        enq(x)
    s = 0
    c = last
    while(c//2>0):
        s += heap[c//2]
        c = c//2
    print('#{} {}'.format(tc, s))
