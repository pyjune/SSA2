def inorder(n, last):
    if(n<=last):
        inorder(n*2, last)
        print(tree[n], end='')
        inorder(n*2+1, last)


T = 10 #int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]
    print('#{}'.format(tc), end=' ')
    inorder(1, N)
    print()
