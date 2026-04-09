import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

T= int(input())

# 델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]
# 다익스트라 함수를 정의
def dijkstra(si,sj):
    # 시작점을 (가중치,도착노드i,도착노드j) 형태로 힙에 넣고 시작
    pq = [(0, si, sj)]
    # fuels: 시작점으로부터 각 노드까지의 연료를 저장될 행렬
    fuels = [[INF]*N for _ in range(N)]
    # fuels 의 시작점을 0으로 넣고 시작
    fuels[si][sj] = 0 

    #while문시작
    while pq:
        # 힙팝을 해서, 그것을 (현재까지의 연료합, 현재노드i, 현재노드j) 의 의미로 사용
        fuel, now_i, now_j = heappop(pq)
        # 팝을 했는데 만약 fuels에 들어있는 값보다 크다면, 넘어간다.
        if fuels[now_i][now_j] < fuel:
            continue
        # 사방으로 탐색한다.
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]
            if ni <0 or ni >= N or nj <0 or nj >= N:
                continue
            # new_fuel: 다음노드에 적힌 연료값
            next_fuel = matrix[ni][nj]
            # use_fuel = 현재에서 다음노드로 갈때 사용한 연료(이게 적혀있는 값으로 해석)
            if next_fuel - matrix[now_i][now_j] > 0:
                use_fuel = next_fuel - matrix[now_i][now_j]
            else:
                use_fuel = 0
            # new_fuel: 다음노드까지 사용한 연료
            new_fuel = fuel + use_fuel + 1
            # 만약 다음노드까지의 누적합이 fuels에 저장된 값보다 크거나 같으면 넘어감.
            if new_fuel >= fuels[ni][nj]:
                continue
            # 이제 넣을 수 있으므로 fuels에 넣기
            fuels[ni][nj] = new_fuel
            # 이제 넣을 수 있으므로 힙푸시
            heappush(pq, (new_fuel, ni, nj))
    # fuels를 리턴
    return fuels


for tc in range(1, 1+T):
    # N: 행렬크기
    N = int(input())
    # INF: 무한대
    INF = 21e8
    # matrix
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # result: 출발점으로부터 각 정점까지의 최단거리가 저장된 리스트
    result = dijkstra(0,0)
    # 결과출력
    print(f"#{tc} {result[N-1][N-1]}")