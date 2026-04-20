import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]

def DFS(si,sj,cnt):
    # 시작점을 현위치로
    now_i = si
    now_j = sj
    
    # 탐색
    for d in range(4):
        next_i = now_i + di[d]
        next_j = now_j + dj[d]
        # 범위 넘어가면 패스
        if next_i < 0 or next_i > N-1 or next_j < 0 or next_j > N-1:
            continue
        # 자신보다 1만큼 커야만 이동
        if matrix[now_i][now_j] + 1 != matrix[next_i][next_j]:
            continue
        # 이제부턴 전진 가능
        # 다음 카운트까지 넘겨주기
        return DFS(next_i,next_j,cnt+1)
    
    return cnt
    
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_counts = 0
    max_i, max_j = 0, 0
    # 일단 시작점 하나로
    # visited는 필요x
    for i in range(N):
        for j in range(N):
            counts = DFS(i,j,1)
            # counts가 최댓값보다 크면 갱신한다
            if max_counts < counts:
                max_counts = counts
                # max_i : 최대카운트일때의 i좌표
                max_i, max_j = i, j
            # 만약 counts가 같다면,
            if max_counts == counts:
                # 맥스를 갱신할필요는 없지만 해당값이 더 작으면 좌표를갱신
                if matrix[max_i][max_j] > matrix[i][j]:
                    max_i, max_j = i, j
    print(f"#{tc} {matrix[max_i][max_j]} {max_counts}")
    

    