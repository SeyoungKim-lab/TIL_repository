# front 와 rear 를 사용하는 방법

# 큐의 크기
N = 10
# 공백상태의 큐를 생성
q = [0] * N
# front, rear 변수 초기화
front = rear = -1
# front : 삭제된 원소의 위치(첫 원소의 위치)
# rear : 마지막 원소의 위치

for i in range(1,11):
    # 삽입 할때는 rear +1 한 자리에 넣는다.
    rear += 1
    q[rear] = i

print(q)
print(front, rear)

for i in range(10):
    # 삭제할때는 front+1 자리에 있는 원소를 삭제
    front += 1
    print(q[front], end=" ")
print()

print(q)
print(front, rear)