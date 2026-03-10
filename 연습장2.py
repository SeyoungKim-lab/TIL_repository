import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1,1+T):

    # NUM : 숫자리스트
    # opertunity : 바꿀기회수
    NUM, opertunity = input().split()
    NUM = list(map(int,NUM))
    opertunity = int(opertunity)
    N = len(NUM)

    for i in range(N):
        max_v = NUM[i]
        for j in range(i+1,N):
            if max_v < NUM[j]:
                max_v = NUM[j]
                J = j   
        if max_v > NUM[i]:  # max_v가 원레보다 커졌으면
            NUM[i], NUM[J] = NUM[J], NUM[i]
            opertunity -= 1
        if opertunity == 0:
            break
    else: # 기회가 남았다면,
        for j in range(10):
            if NUM.count(j) == 2:
                opertunity = 0
                break
        else:   # 같은숫자쌍이 단하나도 없다면
            for k in range(opertunity):
                NUM[-1],NUM[-2] = NUM[-2],NUM[-1]
                opertunity -= 1



            
    



    print(f"#{tc} NUM:{NUM} opertunity:{opertunity}")