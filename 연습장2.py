import sys
sys.stdin = open("input.txt" , "r")

T = int(input())

for tc in range(1, 1+T):
    # N: 맥시노스의 크기
    N = int(input())
    # maxinose: 맥시노스
    maxinose = [list(map(int, input().split())) for _ in range(N)]

    # 1. 문제 이해
    # 2. 나만의 언어로 변환
    # 3. 알고리즘/ 자료구조 선택
    # 4. 검증
    # - 시간/공간 복잡도 계산
    # 5. 구현
    # - 파일 입출력 활용하자

    # 1. 문제이해+나만의언어
    # 맥시노스 안의 코어가 랜덤하게 주어져있다.
    # 코어에 전선을 연결하는데, 직선으로만 연결가능하며, 전선끼리는 교차 불가능하다.
    # 전원은 가장자리에 위치하며, 코어가 가장자리에 있다면 전원 연결된 것으로 간주한다.
    # "최대한 많은 코어에" 전원을 연결하였을 경우, 전선 길이의 합을 구한다.
    # 전선 연결 방법이 여러개가 있다면, 전선길이의 합이 가장 짧은 값을 구한다.
    # (전원이 연결되지 않은 코어가 있을 수도 있다.)

    # 2. 알고리즘/자료구조선택
    # dfs 
    # + 가지치기 (1. 앞으로 남은코어 다더해봤자 최댓값에 못미칠때)
    #   가지치기 (2. 코어갯수같을때 and 길이가 최소길이보다크면)
    # arr = [코어위치를 모아놓은 리스트]
    # 만약 코어 아몰라 일단해보자
    
    # 코어를 모아놓을 리스트
    core_list = []
    # 코어를 모으기
    for i in range(1, N-1):
        for j in range(1, N-1):
            if maxinose[i][j] == 1:
                core_list.append([i,j])
                
    # M: 맥시노스내의 코어갯수
    M = len(core_list)
    
    # 연결된코어의 최대갯수를 저장할 변수
    max_core = 0
    min_wire = float('inf')
                
    # 델타탐색
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    
    def dfs(idx, connect, wire):
        global max_core, min_wire
        
        # 가지치기1: 앞으로 남은 코어를 다 연결해도 최대치 못 넘으면 종료
        if connect + (M - idx) < max_core:
            return
        # 가지치기2: 코어 수 같으면 전선 길이 최소 유지
        
        # 종료조건
        if idx == M:
            if max_core < connect:
                max_core = connect
                return
        
        # 현재 코어 처리
        vi, vj = core_list[idx] # 현코어위치
        
        connected = False   #
        
        for d in range(4):
            # 한 방향마다 path를 초기화
            path = []
            # 방향이 바뀔때마다 현 코어 위치를 다시써주기
            ni, nj = vi, vj
            # 한방향 쭉탐색하기
            while True:  
                ni += di[d]
                nj += dj[d]
                # 한방향 쭉 끝까지가서 끝에 다다르면 다음방향모색
                if not (0<=ni<N and 0<=nj<N):
                    break 
                # 만약 코어나 전선을 만나면 
                if maxinose[ni][nj] != 0:
                    path = []
                    break
                # 한칸씩 이동할때마다 그 위치를 추가해주기
                path.append((ni,nj))
                
            # 가장자리 도달 성공
            if path:
                connected = True

                for x,y in path:
                    maxinose[x][y] = 2

                dfs(idx+1, connect+1, wire+len(path))

                for x,y in path:
                    maxinose[x][y] = 0

        # 연결 안 하는 경우
        dfs(idx+1, connect, wire)
            

    dfs(0, 0, 0)
    # print(f"#{tc} {core_list}")
            