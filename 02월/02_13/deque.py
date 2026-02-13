from collections import deque

# 빈큐 생성
q = deque()
for i in range(1,11):
    q.append(i)

print(q)

for i in range(10):
    print(q.popleft(), end=" ")
print()

print(q)