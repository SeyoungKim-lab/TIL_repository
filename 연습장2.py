import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt", "r")

T = int(input())

def prim(start_node):
    pq = [(0,start_node)]
    MST = [0] * N
    min_weight = 0

    while pq:
        now_weight, now_node = heappop(pq)
        # 이미 방문한 곳이면 패스
        if MST[now_node]:
            continue
        # 현위치에서 방문체크+최소가중치 갱신
        MST[now_node] = 1
        min_weight += now_weight
        # 탐색
        for next_node in range(N):
            # 자기 자신이면 패스
            if next_node == now_node:
                continue
            # 이미 방문한 곳이면 패스
            if MST[next_node]:
                continue
            # next_weight 계산
            next_weight = E * ((x_list[now_node]-x_list[next_node])**2 + (y_list[now_node]-y_list[next_node])**2)
            # 힙에 추가하기
            heappush(pq, (next_weight, next_node))
    return min_weight

for tc in range(1,1+T):
    # N: 섬의개수
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    # E: 환경세율
    E = float(input())

    result = round(prim(0))

    print(f"#{tc} {result}")


