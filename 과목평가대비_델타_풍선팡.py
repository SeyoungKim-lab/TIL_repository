T = int(input())

for tc in range(1,1+T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_pollen = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            # cnt : 행렬의 각 원소의 상하좌우합/ 
            cnt = matrix[i][j]
            # k : 행렬의 각 원소(얼만큼 뻗어나갈 것이냐 의미)
            k = matrix[i][j]

            for d in range(4):
                for c in range(1, 1+k):
                    ni = i + di[d]*c
                    nj = j + dj[d]*c

                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += matrix[ni][nj]

            if max_pollen < cnt :
                max_pollen = cnt
            
    print(f"#{tc} {max_pollen}")