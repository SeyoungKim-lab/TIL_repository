T = int(input())

for tc in range(1, 1+T):

    N, K = map(int,input().split())

    bit = [0] * 12

    counts_ = 0


    for i in range(2):
        bit[0] = i #0번원소
        for j in range(2) :
            bit[1] = j #1번원소
            for k in range(2):
                bit[2] = k #2번원소
                for l in range(2):
                    bit[3] = l
                    for m in range(2):
                        bit[4] = m
                        for n in range(2):
                            bit[5] = n
                            for o in range(2):
                                bit[6] = o
                                for p in range(2):
                                    bit[7] = p
                                    for q in range(2):
                                        bit[8] = q
                                        for r in range(2):
                                            bit[9] = r
                                            for s in range(2):
                                                bit[10] = s
                                                for t in range(2):
                                                    bit[11] = t #11번원소
                                                    # 여기는 모든 부분집합이 형성된상태

                                                    # 1 이 N개인 애들만 뽑고싶음
                                                    counts =0


                                                    for w in bit:

                                                        if w == 1:
                                                            counts +=1
                                                    if counts == N:
                                                        bit_N = bit[:]
                                                        # 여기까진 1이 N개인 애들이 bit_N에 저장된상태

                                                        for aa in range(1,13):
                                                            bit_N[aa-1] = bit_N[aa-1] * aa
                                                        # 여기까지 bit_N 이 제대로 완성됨.
                                                        # print(bit_N)
                                                        su_m = 0
                                                        for ab in bit_N:
                                                            su_m += ab



                                                        if su_m == K :
                                                            counts_ += 1

    print(f"#{tc} {counts_}")
