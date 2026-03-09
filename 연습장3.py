T = int(input())

for tc in range(1,1+T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    di = [1,0]
    dj = [0,1]
    
    def recur(wi,wj, total):
        # 1. 종료조건
        if (wi,wj) == (N-1,N-1):
            print(total)
            return
        # 2. 재귀호출
        # ↓한번, →한번 총 2번호출
        for d in range(2):
            wi = wi + di[d]
            wj = wj + dj[d]
            if 0<=wi<N and 0<=wj<N:
                recur(wi,wj, total + matrix[wi][wj])
            
    
    recur(0,0,matrix[0][0])