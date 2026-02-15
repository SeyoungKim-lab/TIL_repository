T = int(input())

for tc in range(1, 1+T):
    code = input()

    stack = [0] * 40

    top = -1

    pair = {"(" : ")" , "{" : "}"}

    answer = 1

    for c in code:

        if c in "({":
            top += 1
            stack[top] = c

        elif c in ")}":
            
            if top == -1:   #stack안에 아무것도 없으면
                answer = 0
                break

            # stack 안에 뭔가가 있으면
            left = stack[top]
            top -= 1
            if pair[left] != c:
                answer = 0
                break

    if top >= 0:
        answer = 0
    
    print(f"#{tc} {answer}")

                