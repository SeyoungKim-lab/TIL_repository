import sys
sys.stdin = open("input.txt", "r")
from heapq import heappush, heappop


T = int(input())

def dijkstra():
    # 힙 생성
    pq = [(0,0)]
    # dists생성
    dists = [float('inf')] * (N+1)
    # dists에 첫위치 넣어주기
    dists[0] = 0
    # while문 시작
    while pq:
        # 힙팝하며 현위치
        until_now_weight, now_node = heappop(pq)
        # 팝하자마자 dists 확인
        if dists[now_node] < until_now_weight:
            continue
        # 탐색
        for next_weight, next_node in graph[now_node]:
            # new_weight: 탐색위치 까지의 누적가중치
            new_weight = until_now_weight + next_weight
            # dists확인
            if dists[next_node] <= new_weight:
                continue
            # 이제 dists에 넣어주기 + 힙푸시하기
            dists[next_node] = new_weight
            heappush(pq, (new_weight, next_node))
    return dists


for tc in range(1, 1+T):
    # N: 0번에서 N번까지 (총 N+1개)
    # E: 간선의 개수
    N, E = map(int, input().split())
    # 인접리스트 생성
    graph = [[] for _ in range(N+1)]
    # 인접리스트에 채워주기
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
    
    result = dijkstra()

    print(f"#{tc} {result[N]}")
    