import sys
from itertools import combinations
sys.stdin = open("input.txt" , "r")

T = int(input())

for tc in range(1,1+T):
    # N: 재료의 개수
    N = int(input())
    # Sinergy_Matrix: 시너지행렬
    Sinergy_Matrix = [list(map(int,input().split())) for _ in range(N)]

    # 0~ N-1 까지의 재료 중 0은 반드시 포함하고, 나머지 1~N-1 중에 (N/2 - 1)개의 재료를 뽑기
    # 그렇게 A와 B라는 리스트 각각에 대해 2개를 뽑아(2중for문활용)
    # 2개묶음들에 대해 Sinergy_Matrix의 두값(예를들어 S[1][2]와 S[2][1])들을 더하고,
    # 차이에 대한 절댓값(맛의차)을 어떤변수에 저장하고, 그것의 최솟값을 구하기. 

    all_ingredients = set(range(N))

    Pair_sum = [[0] * N for _ in range(N)]
    # 미리 양시너지 합을 계산해둔다.
    for i in range(N):
        for j in range(N):
            if i < j:
                Pair_sum[i][j] = Sinergy_Matrix[i][j] + Sinergy_Matrix[j][i]

    min_v = [float('inf')]

    def comb():

        for A in combinations(range(1,N), N//2 - 1):
            team_a = [0] + list(A)
            team_b = list(all_ingredients - set(team_a))

            taste_A = 0
            taste_B = 0

            
            for i,j in combinations(team_a, 2):
                    taste_A += Pair_sum[i][j]
            for i,j in combinations(team_b, 2):
                    taste_B += Pair_sum[i][j]

                    

            diff_of_taste = abs(taste_A - taste_B)

            min_v[0] = min(min_v[0], diff_of_taste)

            if min_v[0] == 0:
                 return
        return
        


    comb()
    print(f"#{tc} {min_v[0]}")

    