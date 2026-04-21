T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 구상
    
    # 그냥 (2,2) 에서 (4,4) 박스 안에 있는 모든 애들을 뽑아낼 수 있다면..
    # 일단 large_matrix = [[0]*10 for _ in range(10)] 으로 10 x 10 전체매트릭스를 만들어낸다.
    # 그리고 (2,2)에서 (4,4) 의 모든 요소에 1을 더함.
    # 그다음 (3,3)에서 (6,6) 의 모든 요소에 2를 더함.
    # 이때 3인 요소의 갯수를 뽑아내면 됨.
    # 근데 빨강 2개 보라1개 이럴땐 어떻게하느냐.문제에서 배제함.

    large_matrix = [[0] * 10 for _ in range(10)] # 10 X10 매트릭스

    counts = 0 # 3의 개수를 셀 변수



    for k in range(N):
        if matrix[k][4] == 1: # 4열이 1이면 즉, 빨강이면
            
            # 빨간색범위를 large_matrix에서 +1
            for i in range(matrix[k][0],matrix[k][2] + 1): # i 는 2,3,4
                for j in range(matrix[k][1],matrix[k][3] + 1): # j 는 2, 3, 4
                    large_matrix[i][j] += 1

        if matrix[k][4] == 2: # 4열이 2이면 즉, 파랑이면
            
            # 파란색 범위를 large_matrix에서 +2
            for i in range(matrix[k][0],matrix[k][2] + 1): # i 는 2,3,4
                for j in range(matrix[k][1],matrix[k][3] + 1): # j 는 2, 3, 4
                    large_matrix[i][j] += 2
        
    # large_matrix 가 완성된상황. 이제 3의 개수를 세면 끝
    for ii in range(10):
        for jj in range(10):
            if large_matrix[ii][jj] == 3:
                counts += 1

    print(f"#{tc} {counts}")
