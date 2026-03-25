import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,1+T):
    num, op = map(int, input().split())

    num_list = list(map(int, str(num))) # 입력받은 num을 리스트로 변환

    N = len(num_list)   # num의 길이

    max_v = 0

    visited = set() # set내에 특정값이 있는지 빠르게 찾기위해 set을쓴다.

    # op만큼 자리를 다 바꿔보고 max_v에 최댓값을 반환하는 함수.
    def change(depth):
        global max_v

        num_tuple = tuple(num_list)
        # 가지치기
        if (depth,num_tuple) in visited:
            return
        # 가지치기에 안걸렸다면
        visited.add((depth,num_tuple))
        # 종료조건
        if depth == op:
            num_num = int("".join(map(str, num_list)))
            max_v = max(max_v, num_num)
            return
        # 재귀호출
        for i in range(N):
            for j in range(i+1, N):        
                num_list[i], num_list[j] = num_list[j], num_list[i] # 두놈의 자리를 바꾼다.
                change(depth+1)
                num_list[j], num_list[i] = num_list[i], num_list[j]



    change(0)
    print(f"#{tc} {max_v}")