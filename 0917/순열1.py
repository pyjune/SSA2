# 주어진 3개의 숫자로 만드는 순열
def perm(n, k):
    if n==k:
        print(p)
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]

p = [1,2,3]
perm(0, 3)
