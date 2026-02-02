T = int(input()) # 테스트케이스의 개수를 인풋으로 받는다.

for test_case in range(1, T + 1): # 1부터 T까지 순회
 
    N, M = map(int,input().split()) # 전체숫자의 개수를 N에 , 작은배열의 숫자개수를 M에 할당
    arr = list(map(int, input().split())) # 전체 숫자 리스트를 arr에 할당

    max_sum_M = 0 # sum_M의 최댓값을 저장할 변수
    min_sum_M = 10000 * N # sum_M의 최솟값을 저장할 변수 (각숫자는 10000이기에, sum_M은 최대 10000*N까지도 가질 수 있으므로 그보다 크거나같게 설정)

    for i in range(0,N-M+1): # i는 작은배열의 제일왼쪽숫자의 인덱스
        # 이제 각각의 i인덱스에서 출발하여, M개의 숫자를 더해야함.
        sum_M = 0 #
        for j in range(i,i+M): # 각각의 i에 대해서 M개의 인덱스를 순회
            sum_M = sum_M + arr[j]
        # 여기부턴 i에 대한 이미 sum_M이 계산된상황. 그럼 sum_M의 최대,최소를 구하면된다.
        if sum_M > max_sum_M:
            max_sum_M = sum_M
        if sum_M < min_sum_M:
            min_sum_M = sum_M

     
    print(f'#{test_case} {max_sum_M - min_sum_M}')