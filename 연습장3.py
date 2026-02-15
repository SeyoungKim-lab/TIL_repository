T = int(input())

for tc in range(1, 1+T):
    code = input()  # 받을 문자열

    N = len(code)

    stack = [0] * N    

    top = -1

    for c in code:
        
        if top >= 0 and stack[top] == c: # 처음에 -1번인덱스는 걸러지게.
            top -= 1
        
        else:
            top += 1  
            stack[top] = c  # c를 쌓는다.

    # 최종적으로 top+1 이 남은 갯수
    print(f"#{tc} {top +1}")