#           0 1 2 3   col(열)
#       0               
#       1               
#       2               
#       3     c          
#   row(깊이)

# N*N체스판에서 안겹치게 퀸을 두는 경우의 수 구현하기.
# visited[행][열] 로써 visited배열이 행과 열 두가지 정보를 담도록 형성.

def check(row,col):
    #1. 같은 열에 놓은 적이 있는가?
    for i in range(row):
        if visited[i][col]: # 한번이라도 방문했으면
            return True
    #2. 좌상단 대각선에 놓은적이 있는가?
    i, j = row - 1, col - 1
    while i >=0 and j >= 0:
        if visited[i][j]:
            return True
        i -= 1
        j -= 1
    #3. 우상단 대각선에 놓은적이 있는가?
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return True
        i -= 1
        j += 1
    
    return False

def recur(row):
    global answer
    # 1. 종료조건
    if row == N:
        answer += 1
        return
    # 2. 재귀호출
    for col in range(N):    # col: 열번호
        # 유망하지 않는 경우는 못보도록 continue
        # 가지치기
        if check(row,col):
            continue
        # 호출부분
        visited[row][col] = 1
        path.append((row,col))
        recur(row+1)
        path.pop()
        visited[row][col] = 0
        
N = 10       # 판 크기
answer = 0  # 가능한 정답 수
path = []
# N * N 모든 위치의 방문 여부를 기록
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'경우의 수 = {answer}')