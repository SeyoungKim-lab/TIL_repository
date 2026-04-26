import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt", "r")

T = int(input())

# 델타탐색(상,우,하,좌)
di = [-1,0,1,0]
dj = [0,1,0,-1]

# 시작위치찾기함수
def find_start():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'X':
                return i,j

def dijkstra(si,sj,start_dir):
    # 힙생성
    pq = [(0,si,sj,start_dir,0)]
    # dists 생성
    dists = [[float("inf")] * N for _ in range(N)]
    # 첫위치 dists넣기
    dists[si][sj] = 0
    # while문 시작
    while pq:
        # 힙팝하며 현위치
        until_now_weight, now_i, now_j, now_dir, tree_cut_cnt = heappop(pq)
        # 팝한 후 dists확인
        if until_now_weight > dists[now_i][now_j]:
            continue
        # 최초로 Y에 들어오면 종료
        if matrix[now_i][now_j] == 'Y':
            return until_now_weight
        # 탐색
        for d in range(4):
            next_i = now_i + di[d]
            next_j = now_j + dj[d]
            # 범위밖이면 continue
            if next_i < 0 or next_i > N-1 or next_j < 0 or next_j > N-1:
                continue
            # 만약 나무를 만나면
            if matrix[next_i][next_j] == 'T':
                # 나무베기를 다썼다면 continue
                if tree_cut_cnt == K:
                    continue
                # 나무베기가 남아있다면 나무베고 가기
                else:
                    
                    next_tree_cut_cnt = tree_cut_cnt + 1
            # 여기까지 오는경우는, 다음위치가 'G'이거나, 'T'인데 기회가 남아 벤 경우이다.
            # 'T'가 아닌 경우는 나무베기 횟수 차감 x
            
            if matrix[next_i][next_j] == 'G' or matrix[next_i][next_j] == 'Y':
                next_tree_cut_cnt = tree_cut_cnt
            
            if d == now_dir:
                next_weight = 1 # 전진
            elif (d == (now_dir+1)%4       # 보고있는방향에서 오른쪽으로 갈때 
                  or d == (now_dir-1)%4):  # 보고있는 방향에서 왼쪽으로 갈때
                next_weight = 2 # 회전,전진
            elif d == (now_dir+2)%4:    # 반대방향으로 갈때
                next_weight = 3 # 회전,회전,전진
            # 다음방향은 d가된다.
            next_dir = d
            # 누적 가중치
            new_weight = until_now_weight + next_weight
            # 다음 방향에 대한 dists확인
            if new_weight >= dists[next_i][next_j]:
                continue
            # 힙푸시, dists채우기
            dists[next_i][next_j] = new_weight
            
            heappush(pq, (new_weight, next_i, next_j, next_dir, next_tree_cut_cnt))
    # 여기까지온다는건 Y를 못찾았다는 뜻
    return -1
            

for tc in range(1, 1+T):
    # N: 맵의 크기
    # K: 나무베기횟수
    N, K = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    si, sj = find_start()

    result = dijkstra(si,sj,0)

    # for i in range(N):
    print(result)