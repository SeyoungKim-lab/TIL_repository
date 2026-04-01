import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    # N: 구슬쏘는횟수
    # W: 가로길이
    # H: 세로길이
    N, W, H = map(int, input().split())
    # gamepan: 게임판
    gamepan = [list(map(int,input().split())) for _ in range(H)]

    remain_cnt = 0
    for i in range(H):
        for j in range(W):
            if gamepan[i][j] != 0:
                remain_cnt += 1


    # 정리하는 함수
    def organize(copy_gamepan):
        global now_remain
        for j in range(W):              # j는 오른쪽방향으로
            idx = H-1
            for i in range(H-1,-1,-1):  # H-1번부터 0번 인덱스까지 역순회
                if copy_gamepan[i][j] != 0:
                    copy_gamepan[idx][j], copy_gamepan[i][j] = copy_gamepan[i][j], copy_gamepan[idx][j]
                    idx -= 1
        
        return

    # 델타탐색
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    # 해당 열에 떨어뜨린 후에 정리까지 해야함.
    def BFS(w,copy_gamepan):
        global now_remain
        # 열순회로 첫위치찾기
        for i in range(H):
            if copy_gamepan[i][w] != 0:
                si, sj = i, w
                break
        else:
            return
        q = deque([(si,sj,copy_gamepan[si][sj])])
        copy_gamepan[si][sj] = 0
        now_remain -= 1
        while q:
            vi,vj,p = q.popleft()
            for d in range(4):
                for j in range(p):
                    wi = vi + di[d]*j
                    wj = vj + dj[d]*j
                    if 0<= wi < H and 0<= wj < W and copy_gamepan[wi][wj] != 0:
                        q.append((wi,wj,copy_gamepan[wi][wj]))
                        copy_gamepan[wi][wj] = 0
                        now_remain -= 1
        # 다 터뜨렸으면 정리
        organize(copy_gamepan)
        return
    



    min_v = float("inf")
    # W개(0~W-1) 중에 중복순열로 N개를 나열하는 수열
    def permutation(idx):
        global min_v, now_remain
        # 가지치기
        if min_v == 0:
            return
        # 종료조건
        if idx == N:
            now_remain = remain_cnt  # 남은 벽돌수를 저장할리스트
            copy_gamepan = [row[:] for row in gamepan]
            # path에 들어있는 순서대로 BFS를 진행
            for w in path:
                BFS(w,copy_gamepan)
            # BFS는 다 터진후의 게임판copy_gamepan 을 반납
            # 다 터지고 남은 벽돌수 체크
            # for i in range(H):
            #     for j in range(W):
            #         if copy_gamepan[i][j] != 0:
            #             remain_cnt += 1
            min_v = min(min_v, now_remain)
            
            return
        
        # 재귀호출
        for i in range(W):
            path.append(i)
            permutation(idx+1)
            path.pop()

    path = []
    permutation(0)

    print(f"#{tc} {min_v}")
    
    

    
        

    
    
    