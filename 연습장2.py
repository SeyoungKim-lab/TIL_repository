import sys
sys.stdin = open("input.txt", "r")
from heapq import heappush, heappop

T = int(input())

def dijkstra(start_node):
    # 힙생성
    pq = [(0,start_node)]
    # dists 만들기
    dists = [float("inf")] * (N+1)
    # 시작노드 채우기
    dists[start_node] = 1

    # while문시작
    while pq:
        # 힙팝하며시작
        dist, node = heappop(pq)
        # 방금 팝한게 dists의값보다 크면 컨티뉴
        if dist > dists[node]:
            continue
        # 탐색
        for next_dist, next_node in graph[node]:
            # new_dist: 다음 탐색노드까지의 누적거리
            new_dist = dist + next_dist
            # new_dist가 dists의값보다 크거나같으면 컨티뉴
            if new_dist >= dists[next_node]:
                continue
            # 넣을 수 있다면 할 액션 2가지.
            # 1. dists에 넣기
            dists[next_node] = new_dist
            # 2. 힙푸시하기
            heappush(pq, (new_dist, next_node))
    # dists를 반환
    return dists

for tc in range(1, 1+T):
    # N: 0번 부터 N번까지 총 N+1개의 노드
    # E: 도로의 개수
    N, E = map(int, input().split())
    # 인접리스트
    graph = [[] for _ in range(N+1)]
    # 도로 입력받기
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w,e))

    result = dijkstra(0)

    print(f"#{tc} {result[N]}")