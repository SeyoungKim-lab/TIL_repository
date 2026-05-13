import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 서로소집합인 경우 생각하기
def fun():
    global max_v
    for i in range(N):
        if i+max_v > N:
                return
        for j in range(N):
            

            

            if A[i] == B[j]:
                memo = [0] * 2001
                memo[A[i]] += 1
                memo[B[j]] += 1
                cnt = 1
                now_i, now_j = i+1, j+1
                while True:
                    if now_i > N-1 or now_j > N-1:
                        break
                    memo[A[now_i]] += 1
                    memo[B[now_j]] += 1
                    if memo[A[now_i]] >= 4 or memo[B[now_j]] >= 4:
                        break
                    if A[now_i] == B[now_j]:
                        cnt+=1

                        now_i += 1
                        now_j += 1
                    else:
                        now_i += 1
                        now_j += 1
                # 건너띄기가지치기생각
                max_v = max(max_v, cnt)


for tc in range(1,1+T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    

    # 최댓값이 될놈
    max_v = 0
    fun()


    print(f"#{tc} {max_v}")