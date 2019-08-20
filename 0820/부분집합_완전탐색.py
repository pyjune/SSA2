# 합이 10인 부분집합의 개수

def f(i, N, K):
    global cnt
    global bit
    if i==N: #  bit의 모든칸이 결정됨
        s = 0
        for j in range(N): # 0~N-1은 원 집합의 원소 1~N을 가리킴
            if bit[j]==1: # j+1이 부분집합에 포함된 경우
                s += j+1
        if s==K:
            cnt += 1
    else:
        bit[i] = 0
        f(i + 1, N, K)
        bit[i] = 1
        f(i + 1, N, K)




N = 10 # 1부터 N까지가 집합의 원소
K = 10 # 부분집합의 합
cnt = 0
bit = [0] * N
f(0, N, K)
print(cnt)
