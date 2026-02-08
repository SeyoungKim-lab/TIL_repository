T = int(input())

for tc in range(1, 1+T):

    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    sum_matrix = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            # 각 원소에 대해 "4방향의합"을 저장할변수
            sum_4d = 0

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_4d += abs(matrix[i][j] - matrix[ni][nj])
            
            sum_matrix += sum_4d

    print(f"#{tc} {sum_matrix}")
