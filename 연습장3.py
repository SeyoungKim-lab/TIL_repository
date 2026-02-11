T = int(input())





    


for tc in range(1, 1+T):

    postfi = input().split()

    def get_result(postfix):
        stack = []  # 스택을 형성

        for c in postfix:
            if c == ".":
                if not stack or len(stack)>=2:   # 스택안에 꺼낼 숫자가 없으면
                    result = "error"
                    return result
                
                result = stack.pop()
                return result
            if c not in "-+*/":   # c가 숫자면
                stack.append(int(c))
            else:   # c가 연산자면

                if not stack:   # 스택안에 꺼낼 숫자가 없으면
                    result = "error"
                    return result
                
                right = stack.pop() # 스택에서 하나 꺼내서 오른쪽에

                if not stack:   # 스택안에 꺼낼 숫자가 없으면
                    result = "error"
                    return result
                
                left = stack.pop()  # 스택에서 하나 꺼내서 왼쪽에
                
                result = 0
                if c == "+":
                    result = left + right
                elif c == "*":
                    result = left * right
                elif c == "/":
                    result = left // right
                elif c == "-":
                    result = left - right
                
                
                stack.append(result)

    result = get_result(postfi)
    
    print(f"#{tc} {result}")