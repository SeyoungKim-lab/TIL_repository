# 1. 문제상황
# NXM 배추밭이 있는데, 배추는 상하좌우연결되게 심어진다. 연결된 곳이 한 구역.
# 이때 총 몇 구역이 존재하는가?

# 2. 알고리즘/ 자료구조
# 배추밭을 만든다 => NXM 0으로채워진 매트릭스를 만든다.
# 입력을 받아, 배추가 잇는 위치를 1로 채워넣는다.
# 구역의 개수를 셀 변수 counts를 생성한다.
# 배추밭을 for문으로 행우선탐색하여 1의 위치를 찾는다.
# 그 위치에서 dfs탐색을 시작한다. 
# 델타탐색으로 진행하며 방문한 위치는 visited에 표시하고, 
# 그 구역을 다 탐색하면 counts를 1더한다.

T = int(input())

for tc in range(1,1+T):
    # M: 배추밭 가로길이
    # N: 배추밭 세로길이
    # K: 배추심어진갯수
    M, N, K = map(int,input().split())
    # 배추밭 생성
    matrix = [[0]*M for _ in range(N)]
    # K번 배추 입력받아서 배추밭에 넣기
    for i in range(K):
        bj,bi = map(int,input().split())
        matrix[bi][bj] = 1
    # 구역을 셀 갯수 counts
    counts = 0
    # 델타탐색
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    # 방문기록부
    visited = [[0]*M for _ in range(N)]
    # stack
    stack = []
    # 배추밭 행우선탐색 1위치찾기
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not visited[i][j]:
                # dfs탐색
                # vi,vj:현위치
                vi,vj = i, j
                # 시작위치를 방문기록부 찍어주기
                visited[vi][vj] = 1
                while True:
                    

                    for d in range(4):
                        wi = vi + di[d]
                        wj = vj + dj[d]
                        if 0<=wi<N and 0<=wj<M and not visited[wi][wj] and matrix[wi][wj] != 0:
                            stack.append([vi,vj])
                            visited[wi][wj] = 1
                            vi, vj = wi, wj
                            break
                    else:
                        if stack:
                            vi, vj = stack.pop()
                        else:
                            break
                counts += 1

    print(counts)