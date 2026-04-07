import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1,1+T):
    N, W, H = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]

    
    def recur(cnt, remain_block, now_arr):
        global min_v
        # 종료조건+ 가지치기
        if cnt == N or remain_block == 0:
            min_v = min(min_v, remain_block)
            return
        
        # 재귀호출
        for col in range(W):
            # now_arr을 깊은복사하기
            copy_arr = [row[:] for row in now_arr]

            # col 위치에 구슬을 떨어뜨린다 => BFS
            # BFS 시작 위치 찾기
            row = -1
            for r in range(H):
                if copy_arr[r][col]:
                    row = r
                    break
            # 만약 해당 열이 다 0이면 다음구슬로
            if row == -1:
                continue
            # BFS시작
            q = deque([(row, col, copy_arr[row][col])])
            now_remains = remain_block - 1
            copy_arr[row][col] = 0

            while q:
                now_y, now_x, p = q.popleft()

                for d in range(4):
                    for k in range(1,p):
                        ny = now_y + dy[d]*k
                        nx = now_x + dx[d]*k

                        # 범위 밖이면 패스
                        if ny <0 or ny>H-1 or nx <0 or nx>W-1:
                            continue
                        # 0 이면 패스
                        if copy_arr[ny][nx] == 0:
                            continue
                        

                        now_remains -= 1
                        q.append((ny, nx, copy_arr[ny][nx]))
                        copy_arr[ny][nx] = 0
            
            # 정리
            for j in range(W):
                idx = H-1
                for i in range(H-1, -1, -1):
                    if copy_arr[i][j]:
                        copy_arr[i][j], copy_arr[idx][j] = copy_arr[idx][j], copy_arr[i][j]
                        idx -= 1
            
            recur(cnt + 1, now_remains, copy_arr)


    # 처음상태 벽돌개수 세기
    blocks = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    min_v = float("inf")
    recur(0, blocks, arr)

    print(f"#{tc} {min_v}")
    

    # 깨달은점
    # 1. 종료지점에서 액션하지않고, 브랜치에서 액션하기.(왜 더 좋은지는 몰겠음)
    # 2. 지역리스트처럼 활용하려면, 모든 브랜치에서 깊은복사를 해라.
    # 3. 매개변수자체를 건드리면, 같은 depth에서의 형제노드로 이동할때, 왼쪽형제의 정보를 이어받게 된다.
    #    일반적으로 원하는 상황은 depth에서의 고유한 매개변수 이므로,
    #    그렇게 쓰려면 지역리스트처럼 복사해서 수정후 넘겨준다.
    # 4. BFS에서 방문안하는 조건의 순서는 중요하며, 큐에넣고 액션하고의 순서는 중요하다.