import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    # N:원소수
    # K:합
    N, K = map(int, input().split())
    arr = [i for i in range(1,13)]
    cnt = 0
    def bubun(depth, subset, total):
        global cnt
        # 0. 가지치기
        if total > K:
            return
        if len(subset) > N:
            return
        # 1. 종료조건
            # cnt를 증가시켜주자
        if depth == 12:
            if len(subset) == N and total == K:
                cnt += 1
            return
        # 2. 재귀호출
        bubun(depth+1, subset + [arr[depth]], total + arr[depth])
        bubun(depth+1, subset, total)

    bubun(0,[],0,)
    print(f"#{tc} {cnt}")