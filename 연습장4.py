T = int(input())

for tc in range(1, 1+T):
    # cards: 주어진12장의카드
    cards = list(map(int, input().split()))
    
    player1_deque = []
    player2_deque = []
    for i in range(12):
        # 1번플레이어 한개뽑고 베이비진확인
        player1_deque.append(cards.pop(0))
        num_player1_card = len(player1_deque)
        if num_player1_card >= 3:  # 3장이상뽑은경우
            pass
        
        # 2번플레이어 한개뽑고 베이비진확인
        player2_deque.append(cards.pop(0))
        num_player2_card = len(player2_deque)
        if num_player2_card >= 3:
            pass

    path = []
    used = [0] * 6
    baby_gin_result = False

    def is_baby_gin():
        cnt = 0
        # run + triplet 개수의 합 = 2
        # 앞쪽 숫자 3개 체크
        a, b, c = path[0], path[1], path[2]
        if a == b == c:  # triplet
            cnt += 1
        elif a == (b-1) == (c-2):   # run
            cnt += 1

        # 뒤 쪽 숫자 3개 체크
        a, b, c = path[3], path[4], path[5]
        if a == b == c:  # triplet
            cnt += 1
        elif a == (b-1) == (c-2):   # run
            cnt += 1

        return cnt == 2


    def recur(cnt, arr):
        global baby_gin_result
        if cnt == 6:
            # baby-gin 인지 검사
            if is_baby_gin():
                baby_gin_result = True
            return

        for idx in range(len[arr]):
            # idx 를 이미 썼다면 뽑지마라
            if used[idx]:
                continue

            used[idx] = 1
            path.append(arr[idx])
            recur(cnt + 1)
            path.pop()
            used[idx] = 0


    # arr = list(map(int, input().split()))
    # arr = [6, 6, 7, 7, 6, 7]
    arr = [1, 2, 3, 4, 5, 8]
    recur(0)

    print('YES') if baby_gin_result else print('NO')
    
    

def recur(cnt, arr, used):
    global baby_gin_result
    if cnt == len(arr):
        # baby-gin 인지 검사
        if is_baby_gin():
            baby_gin_result = True
        return

    for idx in range(len(arr)):
        # idx 를 이미 썼다면 뽑지마라
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1, arr, used)
        path.pop()
        used[idx] = 0

path = []
A = [1,2,3,4]
N = len(A)
recur(0, A, [0]*N)