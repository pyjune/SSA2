# 합이 10인 부분집합의 개수

def f(i, N, K, s, r):
    global cnt
    global bit
    global cnt2
    cnt2 += 1
    if s == K: # 나머지 원소를 하나라도 추가하면 K보다 커지므로
        cnt += 1
        return
    elif i==N: #모든 원소를 고려했지만 합이 K가 아닌경우
        return
    elif s>K:
        return
    elif s+r<K: #남은 모든 원소를 포함해도 K보다 작은경우
        return
    else:
        f(i + 1, N, K, s, r -(i+1)) # i번이 가리키는 값은 부분집합에 포함하지 않음
        f(i + 1, N, K, s + i+1, r -(i+1)) #i번이 가리키는 값을 부분집합에 포함




N = 20 # 1부터 N까지가 집합의 원소
K = 10 # 부분집합의 합
cnt = 0
cnt2 = 0
bit = [0] * N
f(0, N, K, 0, (1+N)*N//2)
print(cnt2)
