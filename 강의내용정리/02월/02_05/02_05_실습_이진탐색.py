T = int(input())

for tc in range(1, 1+T):
    P, A, B = map(int, input().split())
    # P : 총 페이지수
    # A : A가 찾아야하는 페이지
    # B : B가 찾아야하는 페이지

    # 문제에서 원하는 답 = 누가 더 빨리찾느냐(승자)

    winner = ""

    # A의 이진탐색 범위
    a_start, a_end = 1, P
    # B의 이진탐색 범위
    b_start, b_end = 1, P

    # A와 B가 번갈아 가며 가운데를 찍는다.
    while True:
        # A가 원하는 페이지를 찾았는가 여부
        a_find = False
        # B가 원하는 페이지를 찾았는가 여부
        b_find = False
        # A 또는 B가 원하는 페이지를 찾으면 종료 break
        

        # A가 가운데 페이지 찍어보기
        a_middle = (a_start + a_end) //2
        # 가운데 찍었는데 원하는 페이지 찾은경우
        if a_middle == A : # 검색 성공
            a_find = True
        # 가운데 찍었는데 원하는 페이지보다 작은 경우
        elif a_middle < A :
            a_start = a_middle                
        # 가운데 찍었는데 원하는 페이지보다 큰 경우
        else:
            a_end = a_middle


        # B가 가운데 페이지 찍어보기
        b_middle = (b_start + b_end) //2
        # 가운데 찍었는데 원하는 페이지 찾은경우
        if b_middle == B : # 검색 성공
            b_find = True
        # 가운데 찍었는데 원하는 페이지보다 작은 경우
        elif b_middle < B :
            b_start = b_middle 
        # 가운데 찍었는데 원하는 페이지보다 큰 경우
        else:
            b_end = b_middle

        # A나 B가 원하는 페이지를 찾았으면 승자 결정 하고
       
        # break
        # A가 승
        if a_find == True and b_find == False:
            winner = "A"
            break
        # B가 승
        if a_find == False and b_find == True:
            winner = "B" 
            break
        # A,B 둘다 찾아서 무승부
        if a_find == True and b_find == True:
            winner = 0
            break

        

    print(f"#{tc} {winner}")
