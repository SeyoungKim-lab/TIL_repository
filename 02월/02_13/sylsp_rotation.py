T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = [0] * (N+M+100)
    rear = front = -1

    # arr 의 원소를 맨 앞부터 차례대로 q에 삽입한다.
    for i in range(N):
        rear += 1
        q[rear] = arr[i]


    # q 의 맨 앞에서 원소를 꺼내서 꺼낸 원소를 맨뒤로 삽입하는 연산을 M번
    for i in range(M):
        front += 1
        rear += 1
        q[rear] = q[front]

    # q 의 맨 앞에 있는 원소를 출력
    print(f"#{tc} {q[front+1]}")