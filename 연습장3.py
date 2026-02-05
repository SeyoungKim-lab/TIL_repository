import sys
sys.stdin = open("SUM_input.txt", "r")
sys.stdout = open("SUM_output.txt", "w")

for tc in range(1,11):
    T = int(input())

    # 100 x 100 행렬 형성
    matrix = [list(map(int, input().split())) for _ in range(100)]

    #행의 최댓값을 구하자
    M_row = 0 # 행의 합의 최댓값을 저장할 변수
    for i in range(100): # 행 우선 순회
        sum = 0 # 한 행의 합을 저장할 변수, 행을 순회할때마다 초기화
        for j in range(100):
            sum += matrix[i][j]
        # 여기서 한 행의 합 sum이 계산된 상황. "각 행의합" 의 최댓값을 구해보자.
        if sum > M_row:
            M_row = sum
    # M_row 가 각 행의합의 최댓값이 된 상황




    #열의 최댓값을 구하자
    M_column = 0 # 열의 합의 최댓값을 저장할 변수
    for j in range(100): # 열 우선 순회
        sum2 = 0 # 한 열의 합을 저장할 변수, 열을 순회할때마다 초기화
        for i in range(100):
            sum2 += matrix[i][j]
        # 여기서 한 열의 합 sum2가 계산된 상황. "각 열의합" 의 최댓값을 구해보자.
        if sum2 > M_column:
            M_column = sum2
    # M_column 가 각 열의합의 최댓값이 된 상황



    
    # 오른쪽아래 방향 대각선의 합을 구하자
    down_right_sum = 0
    for i in range(100):
        down_right_sum += matrix[i][i]
    # down_right_sum 이 오른쪽아래 대각선의 합이 된 상황

   

    
    # 왼쪽아래 방향 대각선의 합을 구하자
    down_left_sum = 0
    for i in range(100): 
         down_left_sum += matrix[i][99-i]
    # down_left_sum 이 왼쪽아래 대각선의 합이 된 상황

 


    # 그럼 이제 M_row , M_column , down_right_sum , down_left_sum 중 최댓값을 구하면 된다.
    lst = [M_row , M_column , down_right_sum , down_left_sum]
    max_v = 0
    for k in lst:
        if k > max_v:
            max_v = k
    
    print(f"#{T} {max_v}")
            


    
