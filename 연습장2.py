from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

# visited[x][y][0] => 벽 안부수고 방문
# visited[x][y][1] => 벽 부수고 방문
visited = [[[0,0] for _ in range(M)] for _ in range(N)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1
    
    while queue:
        x, y, broke = queue.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][broke]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M:
                
                # 다음칸이 벽이고 아직 안부쉈다면
                if graph[nx][ny] == 1 and broke == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
                
                # 다음 칸이 빈 칸이고 아직 방문 안했다면
                elif graph[nx][ny] == 0 and visited[nx][ny][broke] == 0:
                    visited[nx][ny][broke] = visited[x][y][broke] + 1
                    queue.append((nx, ny, broke))
    
    return -1
print(bfs())