import sys
sys.stdin = open("input_folder/dijkstra_input.txt", "r")

# 힙 임포트
from heapq import heappush, heappop

# dijkstra 함수 정의
def dijkstra(start_node):
    # 시작할때의 (누적거리,노드번호)를 큐에 삽입
    pq = [(0,start_node)]
    # 각 정점까지의 최단거리를 저장할 리스트 dists
    dists = [INF] * V
    # 시작위치의 최단거리를 dists에 저장
    dists[start_node] = 0
    # while문 시작
    while pq:
        # 힙팝하며 dist, node에 저장
        dist, node = heappop(pq)
        # 리스트dists에 저장된 값보다 방금 팝한 dist가 더 작으면 버린다.
        if dist > dists[node]:
            continue
        # 현 노드로부터 연결된 간선을 탐색
        for next_dist, next_node in graph[node]:
            # 다음노드 까지의 누적거리를 new_dist로 저장
            new_dist = next_dist + dist

            # 만약 다음노드까지의 누적거리가 리스트dists에 저장된 값보다 크면 버린다.
            if new_dist >= dists[next_node]:
                continue

            # 리스트dists에 들어갈 자격이 있다면, 탐색한 노드번호에 누적거리를 삽입해준다.
            dists[next_node] = new_dist
            # 힙에 탐색노드를 push해준다.
            heappush(pq, (new_dist, next_node))
    # dists를 반환
    return dists


# INF 를 무한대로
INF = int(21e8)
# V,E 입력받기
V,E = map(int, sys.stdin.readline().split())
# 시작점 설정
start_node = 0
# graph: 인접 리스트 형성 
graph = [[] for _ in range(V)]
# 간선정보 입력받아 (가중치,도착노드) 형태로 graph에 넣기 (단방향)
for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, end))

# result변수에 dijkstra 함수 실행결과넣기
result = dijkstra(start_node)
# 결과출력
print(result)

