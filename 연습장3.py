T = int(input())

for tc in range(1,1+T):
    # N: 마지막N비트
    # M: 주어진십진수
    N, M = map(int, input().split())
    
    for i in range(N):
        if not M & 1<<i:
            answer = "OFF"
            break
    else:
        answer = "ON"
    print(f"#{tc} {answer}")
    