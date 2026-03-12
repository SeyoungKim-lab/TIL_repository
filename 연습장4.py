#            0 1 2   col(열번호)
#   0    
#   1                   
#   2          c
# row(행번호)

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    
    def check(row,col):
        # 세로확인
        for i in range(row):
            if visited[i][col]:
                return False
        # 왼쪽위대각선확인
        i, j = row -1, col -1
        while i>=0 and j>=0:
            if visited[i][j]:
                return False
            i -= 1
            j -= 1
        # 오른쪽위대각선확인
        i, j = row -1, col +1
        while i>=0 and j<N:
            if visited[i][j]:
                return False
            i -= 1
            j += 1    
        
        # 그곳에 둘 수 있다면
        return True
    # depth: row
    # branch: col
    def Nqueen(row):
        global answer
        # 종료조건
        if row == N:
            answer += 1
            return
        # 재귀호출
        for col in range(N):
            if not check(row,col):
                continue
            visited[row][col] = 1
            path.append((row,col))
            Nqueen(row+1)
            path.pop()
            visited[row][col] = 0
    
    visited = [[0] * N for _ in range(N)]
    path = []
    answer = 0
    Nqueen(0)
    print(f"#{tc} {answer}")
