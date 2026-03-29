import sys
sys.stdin = open("input.txt", "r")

T = int(input())
 
for tc in range(1,1+T):
    # N: 사람수
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 각 사람에 대해서 계단1과 계단2중 어디를 갈건지 선택하게 하는 재귀
    # 모든 사람이 어디를 갈지 결정하고 나면, 
    # 계단1의 도착시간리스트, 계단2의 도착시간리스트를 만들기. 그리고 오름차순정리.
    # 1씩더해줘서 계단을 내려가기 직전 시간으로 다 만들어주고, 
    # 리스트의 인덱스가 2보다 작거나 같을때는 단순히 계단길이를 더해주고,
    # 3보다 크거나 같을때는, 3칸앞의 값보다 크거나 같으면 => 단순히 계단길이 더하고
    # 3칸앞의 값보다 작으면 => 3칸앞값+계단길이를 적어주기.
    # 계단1의 마지막인덱스와 계단2의 마지막인덱스 값중에 더 큰값이 그 경로의 걸린시간이 된다.
    # 그리고 그것의 최솟값 갱신하기.


    people_where = []   # 사람의 좌표담을 리스트
    stair_where_and_length = [] # 계단의 좌표와 길이 담을 리스트

    # 매트릭스를 돌며,
    # 1. 사람의 좌표 담기, 2. 계단의 좌표와 길이 담기(0번계단,1번계단) (i좌표,j좌표,계단길이)
    for i in range(N):
        for j in range(N):
            # 사람이면
            if matrix[i][j] == 1:
                # 사람의좌표를 담기
                people_where.append([i,j])
            # 계단이면
            if matrix[i][j] > 1:
                # 계단의좌표와 길이 담기
                stair_where_and_length.append([i,j,matrix[i][j]])

    people_soo = len(people_where)
    min_v = float("inf")
    # 조합
    def comb(person,path):
        global min_v
        # 종료조건
        if person == people_soo:
            floor0 = [] # 0번계단입구에 도착한 시간들을 모을 리스트
            floor1 = [] # 1번계단입구에 도착한 시간들을 모을 리스트
            # floor0 의 도착시간 리스트와 floor1의 도착시간 리스트 만들기
            for i in range(people_soo):
                # 사람i가 0번계단을 선택한 경우 0번계단 도착시간리스트에 담아주기
                if path[i] == 0:
                    floor0.append(abs(people_where[i][0] - stair_where_and_length[0][0]) + abs(people_where[i][1] - stair_where_and_length[0][1]))
                if path[i] == 1:
                    floor1.append(abs(people_where[i][0] - stair_where_and_length[1][0]) + abs(people_where[i][1] - stair_where_and_length[1][1]))
            floor0.sort()
            floor1.sort()
            
            
            # 입구도착후 1분후로 만들어주기
            floor0 = [x+1 for x in floor0]  
            floor1 = [x+1 for x in floor1]

            
            # 0번계단의 각 사람에 대해 아래층도착시간으로 floor0를 갱신
            for i in range(len(floor0)):
                if i <=2 :
                    floor0[i] = floor0[i] + stair_where_and_length[0][2]
                elif i >2 :
                    if floor0[i] >= floor0[i-3]:
                        floor0[i] = floor0[i] + stair_where_and_length[0][2]
                    else:
                        floor0[i] = floor0[i-3] + stair_where_and_length[0][2]
            
            # 1번계단의 각 사람에 대해 아래층도착시간으로 floor1를 갱신
            for i in range(len(floor1)):
                if i <=2 :
                    floor1[i] = floor1[i] + stair_where_and_length[1][2]
                elif i >2 :
                    if floor1[i] >= floor1[i-3]:
                        floor1[i] = floor1[i] + stair_where_and_length[1][2]
                    else:
                        floor1[i] = floor1[i-3] + stair_where_and_length[1][2]
            # floor0와 floor1의 최댓값 중 더 큰값이 total_time
            if floor0 and floor1:
                total_time = max(floor0[-1],floor1[-1])
            elif floor0:
                total_time = floor0[-1]
            elif floor1:
                total_time = floor1[-1]
            # 모든 경우에 대한 total_time의 최솟값 갱신
            min_v = min(total_time,min_v)

            return
        # 재귀
        comb(person+1, path + [0])  # 0번계단을 선택한경우
        comb(person+1, path + [1])  # 1번계단을 선택한경우

    comb(0,[])

    print(f"#{tc} {min_v}")



    # 계단길이도 담아두기