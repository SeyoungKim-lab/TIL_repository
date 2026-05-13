import heapq

T = int(input())

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

INF = int(1e9)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    land = [input().strip() for _ in range(N)]

    sx = sy = ex = ey = -1
    # tree_idx: 키,벨류 => 트리의위치:몇번째나무
    tree_idx = {}
    # 트리의 개수
    tree_count = 0

    for y in range(N):
        for x in range(N):
            if land[y][x] == 'X':
                sx, sy = x, y
            elif land[y][x] == 'Y':
                ex, ey = x, y
            elif land[y][x] == 'T':
                tree_idx[(x, y)] = tree_count
                tree_count += 1

    # 비트 개수 세기용 캐시
    cut_count = {0: 0}

    def get_bit_count(mask):
        if mask in cut_count:
            return cut_count[mask]
        cnt = 0
        tmp = mask
        while tmp:
            cnt += tmp & 1
            tmp >>= 1
        cut_count[mask] = cnt
        return cnt

    pq = []
    dist = {}

    # (x,y,방향,지금까지벤나무목록)
    start = (sx, sy, UP, 0)
    dist[start] = 0
    # 힙: (누적가중치, x, y, 방향, 지금까지벤나무목록)
    heapq.heappush(pq, (0, sx, sy, UP, 0))

    ans = INF

    while pq:
        cost, x, y, d, mask = heapq.heappop(pq)

        state = (x, y, d, mask)
        if dist.get(state, INF) < cost:
            continue

        if x == ex and y == ey:
            ans = cost
            break

        # 좌회전
        nd = (d - 1) % 4
        nstate = (x, y, nd, mask)
        ncost = cost + 1
        if dist.get(nstate, INF) > ncost:
            dist[nstate] = ncost
            heapq.heappush(pq, (ncost, x, y, nd, mask))

        # 우회전
        nd = (d + 1) % 4
        nstate = (x, y, nd, mask)
        ncost = cost + 1
        if dist.get(nstate, INF) > ncost:
            dist[nstate] = ncost
            heapq.heappush(pq, (ncost, x, y, nd, mask))

        # 전진
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            cell = land[ny][nx]

            # 일반 땅, 시작점, 도착점은 그냥 이동 가능
            if cell != 'T':
                nstate = (nx, ny, d, mask)
                ncost = cost + 1
                if dist.get(nstate, INF) > ncost:
                    dist[nstate] = ncost
                    heapq.heappush(pq, (ncost, nx, ny, d, mask))

            else:
                idx = tree_idx[(nx, ny)]

                # 이미 벤 나무
                if mask & (1 << idx):
                    nstate = (nx, ny, d, mask)
                    ncost = cost + 1
                    if dist.get(nstate, INF) > ncost:
                        dist[nstate] = ncost
                        heapq.heappush(pq, (ncost, nx, ny, d, mask))

                # 아직 안 벤 나무
                else:
                    if get_bit_count(mask) < K:
                        nmask = mask | (1 << idx)
                        nstate = (nx, ny, d, nmask)
                        ncost = cost + 1
                        if dist.get(nstate, INF) > ncost:
                            dist[nstate] = ncost
                            heapq.heappush(pq, (ncost, nx, ny, d, nmask))

    print(f"#{tc} {-1 if ans == INF else ans}")