import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    # 0부터 N-1 까지의 수
    N = int(input())
    golf_area = [list(map(int, input().split())) for _ in range(N)]

    # 1은 첫자리고정, 나머지 수는 수열만들기 + 마지막에 1로 돌아오기까지.
    # branch는 기본적으로 N인데 used배열을 써서 앞에쓴건 못쓰게.
    # total에 golf_area[이전숫자][지금숫자] 를 더해 다음depth에 넘겨준다.
    # depth==0일때는 1고정이므로, depth==1부터 시작.

    used = [0]*N
    # 0은 이미 사용
    used[0] = 1
    min_v = 100*N*N
    def recur(depth, now_room , total):
        global min_v
        # 1. 종료조건
        if 0 not in used:
            total = total + golf_area[now_room][0]
            if min_v > total:
                min_v = total
            return
        # 2. 가지치기
        if min_v < total:
            return

        # 3. 재귀호출
        for next_room in range(N):
            if used[next_room]:
                continue
            used[next_room] = 1
            e_now_to_next = golf_area[now_room][next_room]
            recur(depth+1, next_room, total + e_now_to_next)
            used[next_room] = 0

    recur(0, 0, 0)
    print(f"#{tc} {min_v}")