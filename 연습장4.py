import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    # cost[0]=1일요금, cost[1]=1달요금, cost[2]=3달요금, cost[3] = 1년요금
    cost = list(map(int,input().split()))
    # 0월(깍두기), 1월, 2월, ... , 12월
    schesule = [0] + list(map(int, input().split())) + [0]*3

    # month: 현재월
    # day: 현재월에 이용일수
    # until_now_cost: 전월까지의 누적비용
    min_v = float("inf")
    def recur(month, day, until_now_cost):
        global min_v
        # 가지치기
        if until_now_cost >= min_v:
            return
        # 종료조건
        if month > 12:
            min_v = min(min_v, until_now_cost)
            return
        # 재귀
        # 해당월의 이용계획이 없으면, 다음달로 넘어가라
        if day == 0:
            recur(month+1, schesule[month+1], until_now_cost)
        else:   # 이용계획이 있으면
            # 1일권호출
            recur(month+1, schesule[month+1], until_now_cost + schesule[month]*cost[0])
            # 1달권호출
            recur(month+1, schesule[month+1], until_now_cost + cost[1])
            # 3달권호출
            recur(month+3, schesule[month+3], until_now_cost + cost[2])
            
            
    # 1년계획도 생각할것
    recur(0,0,0)
    answer = min(min_v, cost[3])
    print(f"#{tc} {answer}")
    
        

    
    
    