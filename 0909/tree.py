# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def preorder(n):
    if n>0:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n>0:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])

def postorder(n):
    if n>0:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')

def f(n): # n의 조상 출력하기
    while(par[n] != 0): # n의 부모가 있으면
        print(par[n], end=' ')
        n = par[n]    # 부모를 새로운 자식으로 해서 부모의 부모를 찾으러 감

V = int(input()) # 간선 수 = V - 1
E = V - 1
t = list(map(int, input().split()))

ch1 = [0] * (V+1) #부모를 인덱스로 자식 저장
ch2 = [0] * (V+1)
par = [0] * (V+1) # 자식을 인덱스로 부모 저장

for i in range(E):
    p = t[2*i]
    c = t[2*i+1]
    if ch1[p]== 0: # 아직 ch1 자식이 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p


preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
f(13)
