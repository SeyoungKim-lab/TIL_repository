import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    # N: N*N 격자크기
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    # grid의 어디서 출발해야 가장 많은 방을 방문할 수 있는가?
    # 그때의 출발지점에 적힌값과, 방문방 개수를 출력
    # (단, 방문개수가 같으면 적힌값이 더 작은걸출력)

    # 1커야 이동가능
    # 모든 셀에서 DFS진행, 방문한방의 개수를 기록
    # 방문한방의 최대값을 갱신

    def dfs(r, c):
        # 이미 계산된 적이 있다면 즉시반환
        if memo[r][c] != 0:
            return memo[r][c]
        # 현재위치로 들어오면 일단 1을 기록
        memo[r][c] = 1
        # 이 위치에서 갈 수 있는 곳이 있는지 확인
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                # 다음 방의 숫자가 현재 방의 숫자보다 정확히 1 클 때만 이동
                if room[nr][nc] == room[r][c] + 1:
                    memo[r][c] = dfs(nr,nc) + 1
                    break

        
        
        return memo[r][c]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    memo = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(i,j)

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if max_cnt < memo[i][j]:
                max_cnt = memo[i][j]
                V = room[i][j]
            elif max_cnt == memo[i][j]:
                if V > room[i][j]:
                    V = room[i][j]

    print(f"#{tc} {V} {max_cnt}")


    
        

    
    
    