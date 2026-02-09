T = int(input())

for tc in range(1, 1+T):

    A, B = input().split()

    N =len(A)
    M =len(B)

    # bababa baba
    # 원레하던방식대로면 두번세버리니, 한번 세면 없애버린다.

    # 아니면 for문 말고, i=0부터시작해서, 못찾으면 i+1증가시켜가며 체크.
    # 만약 B를 찾았으면 그만큼 인덱스 증가 시키기

    B_counts = 0
    one_counts = 0

    i = 0
    while i <= N-M+1:
        if B == A[i:i+M]:
            i += M
            B_counts +=1 #B를 찾았을때 카운트
        else:
            i += 1
            one_counts +=1 #B를 못찾았을때 한글자 카운트

    # while문을 탈출했을때 세어야 할게 더 남은경우가 있으므로, remain_cnt에 남은카운트를 저장.
    remain_cnt = N - B_counts * M - one_counts 
    # 그리고 총 카운트를 counts에 저장
    counts = remain_cnt + B_counts + one_counts

    print(f"#{tc} {counts}")