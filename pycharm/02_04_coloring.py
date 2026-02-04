T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 구상
    # 2 2 4 4 1
    # 3 3 6 6 2
    # 빨강(1)= (2,2) 에서 (4,5) 까지 => j는 2에서 4까지, i는 2에서 5까지
    # 파랑(2)= (3,1) 에서 (6,4) 까지 => j는 3에서 6까지, i는 1에서 4까지
    # j는 2에서 4까지를 for문으로 돌며, 그 안에서 3에서 6까지를 for문으로 같은지 확인하고 그것을 뽑아냄.
    # i는 2에서 5까지를 for문으로 돌며, 그 안에서 1에서 4까지를 for문으로 같은지 확인하고 그것을 뽑아냄.
    # 이때 (i,j)를 모은 것이 보라색.
    # 행이 3개인경우는?
    # 빨강(1) 2개와 파랑(2)1개면, for 빨강에 대해 for 파랑을 검토하고,
    # 모든 보라색 (i,j)를 하나의 리스트에 넣고, set함수를 써서 중복을 제거한다.

    # 그냥 (2,2) 에서 (4,4) 박스 안에 있는 모든 애들을 뽑아낼 수 있다면..
    # 일단 large_matrix = [[0]*10 for _ in range(10)] 으로 10 x 10 전체매트릭스를 만들어낸다.
    # 그리고 (2,2)에서 (4,4) 의 모든 요소에 1을 더함.
    # 그다음 (3,3)에서 (6,6) 의 모든 요소에 2를 더함.
    # 이때 3인 요소의 갯수를 뽑아내면 됨.
    # 근데 빨강 2개 보라1개 이럴땐 어떻게하느냐.문제에서 배제함.

    large_matrix = [[0] * 10 for _ in range(10)]



    for k in range(N):
        if matrix[k][4] == 1: # k는 matrix의 행이고, 4열이 빨강이면

            for i in range(large_matrix[k][0],large_matrix[k][2] + 1): # i 는 2,3,4
                for j in range(large_matrix[k][1],large_matrix[k][3] + 1): # j 는 2, 3, 4
                    large_matrix[i][j] += 1

    print(large_matrix)
