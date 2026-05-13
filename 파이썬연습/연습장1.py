import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

T= int(input())


def prim(start_node):
    # pq 생성
    pq = [(0, start_node)]
    # MST 생성
    MST = [0] * (V+1)
    # 최소가중치
    min_weight = 0

    # while문 시작
    while pq:
        # 힙팝하며 현위치
        now_weight, now_node = heappop(pq)
        # 팝하자마자 MST확인
        if MST[now_node]:
            continue
        # 현위치에서 MST채우고, 최소합 갱신
        MST[now_node] = 1
        min_weight += now_weight
        # 탐색
        for next_weight, next_node in graph[now_node]:
            # MST 확인
            if MST[next_node]:
                continue
            # 힙푸시
            heappush(pq, (next_weight, next_node))
    return min_weight

for tc in range(1, 1+T):
    # 0에서 V까지
    V, E = map(int, input().split())
    # 인접리스트
    graph = [[] for _ in range(V+1)]
    # 인접리스트에 입력받기
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    
    result = prim(0)

    print(f"#{tc} {result}")