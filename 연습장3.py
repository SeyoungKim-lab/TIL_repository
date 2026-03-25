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