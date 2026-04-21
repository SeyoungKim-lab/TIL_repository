import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def recur(now_i,now_j, total):
        global min_v
        # 가지치기
        if min_v <= total:
            return
        # 종료조건
        if (now_i, now_j) == (N-1,N-1):
            min_v = min(min_v, total)
            return
        # 재귀호출
        for d in range(2):
            next_i = now_i + di[d]
            next_j = now_j + dj[d]
            if 0<= next_i <N and 0<= next_j<N:
                recur(next_i, next_j, total + matrix[next_i][next_j])
            
    
    min_v = 10*N*N
    di = [1, 0]
    dj = [0, 1]
    recur(0,0, matrix[0][0])
    print(f"#{tc} {min_v}")