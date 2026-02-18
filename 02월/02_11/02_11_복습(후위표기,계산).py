# 중위표기법(infix) => 후위표기법(postfix)

# 우선순위 표 ( 스택밖: icp), (스택안: isp)
icp = {"+":1 , "-":1, "*":2, "/":2 , "(":3}
isp = {"+":1 , "-":1, "*":2, "/":2 , "(":0}

# infix :바꾸고 싶은 중위표기법
# n :식의 길이
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
    stack = []

    # infix 에서 한글자씩 떼어와서 식을 만들자
    for i in range(n):
        # i번째 글자 확인
        # 연산자? 피연산자?
        if infix[i] not in "()+-*/":
            # i번 글자가 연산자 아니였다.(숫자)
            # 결과로 출력(후위표기식에)
            postfix += infix[i]
        else:
            # i번 글자가 연산자였다
            # i번 글자가 오른쪽괄호(닫는괄호)
            if infix[i] == ")":
                # 여는 괄호가 나올때까지 스택에서 연산자 계속 pop
                # () 안의 연산자가 먼저 연산되어야 하기 때문에
                # 꺼내서 쓴다. ( 식에 먼저 써줘야함)
                while stack:
                    # 연산자 꺼내기
                    op = stack.pop()
                    # 여는 괄호 만나면 중단
                    if op == "(":
                        break
                    # 후위표기식에 써주기
                    postfix += op
            else:
                # i번 글자가 닫는괄호가 아닌 연산자
                # i번 글자의 우선순위를 알아내서 (icp[infix[i]])
                # 스택의 꼭대기에 있는 연산자와 비교 (isp[stack[-1])
                # icp[infix[i]] 애랑 isp[stack[-1]] 비교

                # 1. 현재 i번 글자의 연산자의 우선순위보다
                # 스택의 꼭대기에 있는 우선순위가 같거나 높다면
                # i번 글자보다 우선순위가 같거나 높은 애들은 스택에서 모두 꺼내쓴다.
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop()
                
                # 2. 현재 i번 글자의 연산자의 우선순위가
                # 스택의 꼭대기에 있는 우선순위보다 높다면
                # 스택에 push
                stack.append(infix[i])

    # 스택에 연산자가 남아있다면 다 꺼내서 쓰면 된다.
    while stack:
        postfix += stack.pop()

    return postfix

infix = "6+5*(2-8)/2"
postfix = get_postfix(infix, len(infix))
print(postfix)

def get_result(postfix):
    # 후위표기식 계산방법
    # 앞에서부터 쭉 한번만 보면 된다.
    # 숫자를 만나면 스택에 넣고
    # 연산자를 만나면 먼저 나온애 오른쪽, 나중에 나온애 왼쪽 두개 꺼내서
    # 연산하고 그 결과 다시 스택에 넣기
    stack = []

    for c in postfix:
        # 글자 하나 떼어와서 c 라고 하면
        # c가 숫자인가 연산자인가
        if c not in "+-*/":
            # 타입 조심
            stack.append(int(c))
        else:
            # c가 연산자면
            # 스택에서 두개꺼내서 연산
            right = stack.pop() # 먼저 꺼낸애는 연산자 오른쪽
            left = stack.pop()  # 나중에 꺼낸애는 연산자 왼쪽

            result = 0
            # 연산자의 종류에 따라 계산
            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left / right   # 연산결과가 실수
            
            # 이 연산결과를 다시 다른 연산자의 피연산자로 써야하니
            # 스택에 push
            stack.append(result)
    
    # 모든 식을 다 확인했다면 스택에 숫자 1개 남아있다 (최종 연산 결과)
    return stack.pop()

result = get_result(postfix)
print(result)