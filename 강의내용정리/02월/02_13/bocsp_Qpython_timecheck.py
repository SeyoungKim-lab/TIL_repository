import time

N = 200000

start = time.time()

#1. 파이썬의 리스트메서드
q1 = []

for i in range(N):
    q1.append(i)

for i in range(N):
    q1.pop(0)

end = time.time()

print(f"1번걸린시간: {end-start:0.5f}")

#2. front, rear 사용
start = time.time()

q2= [0] * N
front = rear = -1

for i in range(N):
    rear +=1
    q2[rear] = i
    
for i in range(N):
    front +=1

end = time.time()

print(f"2번걸린시간: {end-start:.5f}")