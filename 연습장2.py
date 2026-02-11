T = 10

for tc in range(1, 1+T):

    N = int(input())    # 계산식의길이
    infix = input()
    postfix = ""
    stack = []

    for token in infix:
        if token != "+" : # 숫자면
            postfix += token
        else: # + 이면
            if not stack or  :
                stack.append(token)
