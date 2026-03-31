import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    candy = list(map(int, input().split()))
    answer = -1
    if candy[1] >=2 and candy[2] >= 3:
        answer = 0
        if candy[1] > candy[2] - 1:
            answer += candy[1] - (candy[2] - 1)
            candy[1] = candy[2] - 1
        if candy[0] > candy[1] - 1:
            answer += candy[0] - (candy[1] - 1)
    print(f"#{tc} {answer}")
    
    