'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0] * 10    # 스택을 형성
top = -1            # top에 -1을 넣음 (=아직 스택에 아무것도 없다.)

icp = {'(':3 , '*':2 , '/':2 , '+':1 , '-':1} # 스택밖에서의 우선순위 #왜?
isp = {'(':0 , '*':2 , '/':2 , '+':1 , '-':1} # 스택안에서의 우선순위

infix = '(6+5*(2-8)/2)' # 중위식 문자열 
postfix = ''            # 후위식 문자열

for token in infix:              # 중위식 문자열을 순회한다. 각각의 요소가 token.
    if token not in '(*/+-)':    # 피연산자면(=숫자면)
        postfix += token         # 후위식 문자열에 추가
    elif token == ')':          # 닫는 괄호면 여는 괄호를 만날 때까지 pop
        while top>-1 and stack[top] != '(': # 스택안에 뭔가가있고, 스택의top이 여는괄호가 아니면
            postfix += stack[top]    # 스택의top요소를 후위식문자열에 추가하고,
            top -= 1   # 스택top요소 한개를 버린다.
        # while stack and stack[-1] != '(':     #어펜드,팝이용한경우
        #     postfix += stack.pop()    
        if top != -1:   # 스택안에 여는괄호가 있는경우
            top -= 1        # '(' 제거
    else:                   # '(*/+-'인 경우
        if top == -1 or isp[stack[top]] < icp[token]:   #스택안에 아무것도 없거나, 방금받은token의 우선순위가 스택안의 top우선순위보다 높으면
            top += 1    # top을 한단계 올려놓고
            stack[top] = token  # 거기에 token을 넣는다
        elif isp[stack[top]] >= icp[token]: # 방금받은token보다 stack[top]의 우선순위가 더 높거나 같으면
            while top > -1 and isp[stack[top]] >= icp[token]:  # token이 stack[top]보다 더 높은 우선순위를 가질 때까지
                top -= 1    # 스택한개를버리고
                postfix += stack[top + 1]     # 그것을 후위식문자열에 추가한다.   
            top += 1            # 스택의 마지막 연산자보다
            stack[top] = token  # 우선순위가 높아졌으므로 push

print(postfix)

stack = []  #빈 스택을 생성
for token in postfix:   # 후위문자열을 순회하며
    if token not in '*/+-': #피연산자(=숫자) 면 push
        stack.append(int(token))    #token은 문자열
    else:                   # 연산자면
        op2 = stack.pop()   # 오른쪽 피연산자
        op1 = stack.pop()   # 왼쪽 피연산자
        result = 0
        if token == '*':
            result = op1*op2
        elif token == '/':
            result = op1/op2
        elif token == '+':
            result = op1+op2
        elif token == '-':
            result = op1-op2
        stack.append(result)
answer = stack.pop()
print(answer)
