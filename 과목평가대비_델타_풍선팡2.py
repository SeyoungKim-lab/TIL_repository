T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최대 꽃가루개수
    max_pollen = 0
    #델타탐색이고, 상하좌우순서
    di = [-1, 1, 0 ,0]
    dj = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(M):
            # 행렬의 각 원소의 상하좌우합
            cnt = matrix[i][j]

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                
                # ni,nj가 유효한 범위에 있을때만 합을갱신
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += matrix[ni][nj]

            if max_pollen < cnt:
                max_pollen = cnt

    print(f"#{tc} {max_pollen}")