T = int(input())

for tc in range(1, 1+T):
    N_A , N_B = map(int, input().split()) #N_A는 수열A의 원소개수, N_B는 수열B의 원소개수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #일단 수열B를 순회하며 ..
    #강사님아이디어는 A를 순회하며 어떤조건을 만족시키면 B가움직이는
    # while문 사용해서 해보기
    # import sys
    # sys.stdin = open("sample.txt", "r")