T = int(input())

for tc in range(1, 1+T):

    code = input()

    stack = []

    pair = {"(" : ")" , "{" : "}"}

    answer = 1

    for c in code:

        if c in "({":
            stack.append(c)
        
        if c in ")}":

            if not stack:
                answer = 0
                break

            left = stack.pop()
            if pair[left] != c:
                answer = 0
                break
        
    if stack:
        answer = 0
    
    print(f"#{tc} {answer}")