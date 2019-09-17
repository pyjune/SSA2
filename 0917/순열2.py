# 주어진 5개의 숫자 중 3개를 골라 만드는 순열
def perm(n, k, m):
    if n==k:
        print(p[:3])
    else:
        for i in range(n, m):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k, m)
            p[n], p[i] = p[i], p[n]

p = [1,2,3,4,5]
perm(0, 3, 5)
