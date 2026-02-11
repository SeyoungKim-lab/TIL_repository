T = int(input())

for tc in range(1, 1+T):
    # 미로의 크기 N
    N = int(input())
    
    maze = [list(map(int,input())) for _ in range(N)] # 미로를 받는다

    si, sj = 0, 0   # 시작 위치

    # 미로를 모두 돌며 2찾아 시작위치로 설정
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j   

    # 상하좌우 순으로 델타탐색할거 저장
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    def dfs(si,sj):

        # 방문기록부
        visited = [[0]*N for _ in range(N)]

        # 돌아올 곳을 남긴다. 호랑이는가죽을남기고 어쩌고
        stack = []

        # 시작지점에 방문도장을 찍어놓는다.
        visited[si][sj] = 1

        # i, j 는 현위치로써 사용할 것임. 일단 시작위치를 현위치로설정.
        i,j = si, sj 

        while True:

            if maze[i][j] == 3: # 현위치가 종료지점이면
                return 1    # 1을반환
            
            for d in range(4):
                # ni,nj 는 탐색할 위치
                ni = i + di[d]
                nj = j + dj[d]

                # 탐색위치가 유효범위이고, 방문했던곳이 아니고, 벽이 아니면
                if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and maze[ni][nj] != 1:
                    # 탐색위치에 방문도장을 찍고
                    visited[ni][nj] = 1
                    # 스택에 현위치를 넣어두고
                    stack.append((i,j))
                    # 현위치를 갱신한다.(=이동한다)
                    i, j = ni, nj
                    break   # for을 탈출 => while문을 다시 돈다.(=다시 탐색한다.)
            
            else:
                # for문이 break없이 정상적으로 4번다 돌았을때 실행. 
                # 그말은 즉슨, 탐색을 했더니 이동할 곳이 없다.

                if stack:   # 스택에 뭔가가 남았다면
                    i, j = stack.pop()  # 스택에서 pop해서 그 위치로 이동한다.
                else:   # 스택에 뭔가가 없다면
                        # 돌아갈 곳이 없다. 즉, 시작지점으로 다시 온것임.(결국 종료지점으로 갈 수 없다는뜻)
                    return 0 # 0을 반환한다.
    
    result = dfs(si,sj)
    
    print(f"#{tc} {result}")