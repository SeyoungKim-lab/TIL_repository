T = int(input())

for tc in range(1, T+1):
    
    # 1. 무게 중에 가장 큰놈을 담을 수 있는지 적재용량 큰거부터 체크
    # 2. 담을 수 있다면 담은무게를 어떤 변수에 더해주고 그 적재용량은 0으로 만들어버리기.
    
    # N: 컨테이너수
    # M: 트럭수
    N, M = map(int, input().split())
    # W_lst : 컨테이너 무게리스트
    # t_lst : 트럭 적재용량 리스트
    W_lst = list(map(int,input().split()))
    t_lst = list(map(int,input().split()))
    
    W_lst.sort(reverse=True)
    t_lst.sort(reverse=True)
    
    total_w = 0
    
    for i in range(N):
        for j in range(M):
            if W_lst[i] <= t_lst[j]:  # 담을 수 있으면
                total_w += W_lst[i]   # 담기
                t_lst[j] = 0          # 담은 트럭은 못쓰니까 0으로 만들기
                break   # 다음 i로 넘어가야함
    
    
    print(f"#{tc} {total_w}")