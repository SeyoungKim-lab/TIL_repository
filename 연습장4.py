import sys, copy
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

    start_cnt = 0
    for i in range(H):
        for j in range(W):
            if gamepan[i][j] != 0:
                start_cnt += 1
    # 카피게임판 형성: 얘를 가지고 놀다가 하나의 path가 끝나면 초기화시킬 예정
    copy_gamepan = copy.deepcopy(gamepan)

    # 델타탐색
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    # 해당 열에 떨어뜨린 후에 정리까지 해야함.
    def BFS(w):
        # 열순회로 첫위치찾기
        for i in range(H):
            if copy_gamepan[i][w] != 0:
                si, sj = i, w
                break
        q = deque([(si,sj)])

        while q:
            vi,vj = q.popleft()
            v = copy_gamepan[vi][vj]
            copy_gamepan[vi][vj] = 0
            for d in range(4):
                for j in range(v):
                    wi = vi + di[d]*j
                    wj = vj + dj[d]*j
                    if 0<= wi < H and 0<= wj < W and copy_gamepan[wi][wj] != 0:
                        q.append((wi,wj))
        # 다 터뜨렸으면 정리


    



    min_v = float("inf")
    # W개(0~W-1) 중에 중복순열로 N개를 나열하는 수열
    def permutation(idx):
        # 종료조건
        if idx == N:
            remain_cnt = 0  # 남은 벽돌수를 저장할리스트
            
            # path에 들어있는 순서대로 BFS를 진행
            for w in path:
                BFS(w)
            # BFS는 다 터진후의 게임판copy_gamepan 을 반납
            # 다 터지고 남은 벽돌수 체크
            for i in range(H):
                for j in range(W):
                    if copy_gamepan[i][j] != 0:
                        remain_cnt += 1
            min_v = min(min_v, remain_cnt)

            # 다음 path를 위해 카피게임판을 초기화
            copy_gamepan = copy.deepcopy(gamepan)
            return
        
        # 재귀호출
        for i in range(W):
            path.append(i)
            permutation(idx+1)
            path.pop()

    path = []
    # permutation(0)
    BFS(2)
    BFS(2)
    max_pang = start_cnt - min_v
    for i in range(H):
        print(f" {copy_gamepan[i]}")
    
    

    
        

    
    
    