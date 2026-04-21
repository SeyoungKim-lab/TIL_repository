def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES 

    if k == n:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c)  # c = {True, False}
        for i in range(ncandidates):    # ncandidates == 2
            a[k] = c[i]                 
            backtrack(a, k + 1, n)      
            

            # backtrack(a=[0,0,0], k=0 , n=3)시작
            # [True ,0 ,0]
            # [True, True, 0]
            # [True, True, True] => n==k => 출력
            # 덜끝난 for문에 의해 [True, True, Flase] => n==k => 출력
            # False까지 끝난 k==2인 함수는 종료.
            # 덜끝난 for문에 의해 [True, False, False] => 

def construct_candidates(a, k, n, c):  # 후보 추천
    c[0] = True  # 원소의 포함 여부
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 2   
NMAX = 3
a = [0] * NMAX      # [True, False, True] 이런거
num = [1, 2, 3]
backtrack(a, 0, 3)
