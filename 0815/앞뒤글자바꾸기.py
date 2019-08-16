# 앞뒤 글자 바꾸기
s = list(input()) # 'ABCD' -> 'A', 'B', 'C', 'D'
# 'A' <-> 'D', 'B'<->'C', 총 교환 횟수는 글자수//2
#        0    1    2    3 <- len(s)-1
# s = [ 'A', 'B', 'C', 'D' ]
for i in range(0, len(s)//2): # 4//2 -> 2회, 인덱스 0, 1
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
for i in range(0, len(s)):
    print(s[i], end='')
#print()
#print(''.join(s))
