import sys
from heapq import heappush, heappop

sys.stdin = open("input.txt", "r")

T = int(input())

# 델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]

def dijkstra(si,sj):
    # 힙생성
    pq = [(0,si,sj)]    # (가중치,현i,현j)
    # dists 만들기
    dists = [[float("inf")] * N for _ in range(N)]
    # dists에 첫위치넣기
    dists[si][sj] = 0
    # while문 시작
    while pq:
        now_dist, now_i, now_j = heappop(pq)
        # 현 위치가 dists에 적힌 값보다 크면 continue
        if dists[now_i][now_j] < now_dist:
            continue
        # 탐색
        for d in range(4):
            next_i = now_i + di[d]
            next_j = now_j + dj[d]
            # 범위밖이면 컨티뉴
            if next_i < 0 or next_i > N-1 or next_j < 0 or next_j > N-1:
                continue
            # difference_of_height = 높이차
            difference_of_height = matrix[next_i][next_j] - matrix[now_i][now_j]
            # 만약 다음산이 더 높으면
            if difference_of_height > 0:
                # new_dist는 now_dist에 차이만큼 더해준다.(이동가중치도 +1)
                new_dist = now_dist + difference_of_height + 1
            else:   # 만약 다음산이 더 낮거나, 같으면
                # new_dist는 이동가중치만 더해준다
                new_dist = now_dist + 1
            # new_dist가 dists에 적힌 값보다 크거나 같으면 컨티뉴
            if new_dist >= dists[next_i][next_j]:
                continue
            # 이제 dists에 넣을 수 있고, 힙푸시 하면된다.
            dists[next_i][next_j] = new_dist
            heappush(pq, (new_dist, next_i, next_j))
    # dists를 리턴
    return dists
for tc in range(1, 1+T):
    # N: 행렬의 크기
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(0,0)

    print(f"#{tc} {result[N-1][N-1]}")