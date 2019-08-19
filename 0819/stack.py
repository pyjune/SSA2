#크기가 정해진 리스트를 사용한 스택 구현
stack = [0]*10
top = -1

#push(1)
top = top + 1
stack[top] = 1
#push(2)
top = top + 1
stack[top] = 2
#push(3)
top = top + 1
stack[top] = 3

#pop()
r = stack[top]
top = top - 1
print(r)

while(top != -1): # 스택이 비어있지 않으면 반복
    r = stack[top]
    top = top - 1
    print(r)

#append()를 사용한 스택
s = list()
s.append(10)
s.append(20)
s.append(30)
while(len(s)!=0):
    print(s.pop())

