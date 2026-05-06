import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 대표찾기함수
def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

# 합치기함수
def union(x,y):
    rep_x = find_set(x)
    rep_y = find_set(y)
    if rep_x == rep_y:
        return

    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y
    return


for tc in range(1, 1+T):
    # N: 1번부터 N번까지의 번호
    # M: 신청서개수
    N, M = map(int, input().split())

    # make_set
    parents = [x for x in range(N+1)]

    # 신청서 받기
    sinchung = list(map(int, input().split()))

    for i in range(0,len(sinchung),2):
        x = sinchung[i]
        y = sinchung[i+1]

        # 합치기
        union(x,y)
    # find_set 전체정리
    for x in range(1,N+1):
        find_set(x)
    # 빈 set 생성하고, 거기에 대표 넣기.
    rep_set = set()
    for x in range(1, N+1):
        rep_set.add(parents[x])
    # 만들어진 set의 원소개수 세기
    answer = len(rep_set)
    print(f"#{tc} {answer}")
        