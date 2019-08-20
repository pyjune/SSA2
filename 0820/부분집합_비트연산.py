# 합이 10인 부분집합의 개수
N = 20
K = 10
cnt = 0
arr = [i for i in range(1, N+1)]
for i in range(1, 1<<N):
    s = 0
    for j in range(N): # 0에서 9번 비트까지 검사
        if i & (1<<j):
            s += arr[j]  # j번이 부분집합에 포함되면..
            # s += j+1 # 인덱스를 직접 부분집합의 숫자로 활용
    if s == K:
        cnt = cnt + 1
print(cnt)
