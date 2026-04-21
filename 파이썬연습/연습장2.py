import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]

def DFS(now_i, now_j, oppertunity, now_length):
    global maximum_length
    # 매번 최대길이 갱신
    maximum_length = max(maximum_length, now_length)
    # 탐색
    for d in range(4):
        next_i = now_i + di[d]
        next_j = now_j + dj[d]
        # 범위 벗어나면 컨티뉴
        if next_i < 0 or next_i > N-1 or next_j < 0 or next_j > N-1:
            continue
        # 방문한적있으면 컨티뉴
        if visited[next_i][next_j]:
            continue
        # 나보다 크거나 같으면
        if matrix[next_i][next_j] >= matrix[now_i][now_j]:
            # 기회가 없다면 컨티뉴
            if oppertunity == False:
                continue
            # 근데 기회가 남아있다면?
            elif oppertunity == True:
                # 깎았을 때 갈 수 있는지 본다.
                cutted_height = matrix[next_i][next_j] - K  # 다음위치를 깎아봤을때의 높이
                # 깎았을 때 갈 수 있다면
                if cutted_height < matrix[now_i][now_j]:
                    # 임시저장
                    temp = matrix[next_i][next_j]
                    # 깎고(최대로 깎지말고, 현재보다 1만 작게 깎는다.=>그래야 최장길이보장)
                    matrix[next_i][next_j] = matrix[now_i][now_j] - 1
                    # 이동한다.
                    visited[next_i][next_j] = 1     # 이동하기 전 방문체크
                    DFS(next_i, next_j, False, now_length+1)
                    visited[next_i][next_j] = 0     # 되돌리기
                    matrix[next_i][next_j] = temp   # 깎은거 되돌리기
                    
                # 깎았는데 갈 수 없다면 컨티뉴
                else:
                    continue
        # 나보다 작으면
        else:
            # 그냥 다음 방향으로 이동한다.
            visited[next_i][next_j] = 1     # 이동하기 전 방문체크
            DFS(next_i, next_j, oppertunity, now_length+1)
            visited[next_i][next_j] = 0     # 되돌리기

for tc in range(1, 1+T):
    # N: 부지의 크기
    # K: 최대 깎을 수 있는 높이
    N, K = map(int, input().split())
    # matrix: 부지
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # visited
    visited = [[0]*N for _ in range(N)]
    # 최장등산로길이
    maximum_length = 0

    max_v = 0
    # 시작위치 찾기1. max값 찾기
    for i in range(N):
        for j in range(N):
            max_v = max(max_v, matrix[i][j])
    # 시작위치 찾기2. max값 있는 위치 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_v:
                # si,sj가 시작위치
                si, sj = i, j
                # DFS 진행
                visited[si][sj] = 1
                DFS(si,sj,True,1)
                visited[si][sj] = 0

    # 진행하고나면, maximum_length 가 갱신되어있을것임.
    print(f"#{tc} {maximum_length}")
    
