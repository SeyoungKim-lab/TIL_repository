T = int(input())

for tc in range(1, 1+T):
    # 세로 길이 N, 가로길이 M
    N, M = map(int, input().split())

    # 2차원 배열 입력받기
    # 한줄에 1차원 배열 하나
    # N줄
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 행 우선 순회 [0][0]-[0][1]-[0][2]...[1][0]
    # i를 행번호, j를 열번호
    for i in range(N):
        for j in range(M):
            answer += matrix[i][j]

    print(f"#{tc} {answer}")