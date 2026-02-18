T = int(input())

for tc in range(1,1+T):

    N = int(input())

    maze = [list(map(int,input()))  for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    stack = []

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    answer = 0

    # 시작위치 찾기 함수
    def find_start():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    
                    return i,j
    
                
    # dfs탐색함수
    def dfs_func(si,sj):
        global answer
        
        vi, vj = si, sj # 현위치
        
        visited[vi][vj] = 1

        while True:
            for d in range(4):
                wi = vi + di[d]
                wj = vj + dj[d]
                if 0<= wi < N and 0<= wj <N and not visited[wi][wj] and maze[wi][wj] != 1 :
                    visited[wi][wj] = 1
                    stack.append([vi,vj])
                    vi, vj = wi, wj
                    break   # for문을 끝낸다 = 그 위치에서 다시 탐색한다.
            else:   # 갈데가 없다
                if maze[vi][vj] == 3:
                    answer = 1
                    return
                else:
                    if not stack:
                        return
                    
                    vi, vj = stack.pop()
                    
                       

            
        
    si, sj = find_start()
    dfs_func(si,sj)

    print(f"#{tc} {answer}")