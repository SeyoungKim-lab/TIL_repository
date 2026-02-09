# top 이라는 키워드와 (크기가 고정된)배열을 활용한 스택

# 스택초기화(선언)
# top : 스택에 마지막으로 삽입된 자료의 위치(인덱스)를 나타냄
top = -1
# N : 스택의 크기
N = 10
# 리스트로 스택을 만들기
stack = [0] * N


# 스택에 자료 삽입하기
for i in range(1, 10):
    top += 1
    stack[top] = i

# 스택에 자료를 추가하기 전에 스택이 꽉 찼나 확인
if top < N-1 :
    # 넣을 수 있다면 추가
    top += 1
    stack[top] = 11
else: # 스택에 더이상 원소를 넣을 수 없음
    print("overflow")

print(stack, top)

# 스택에서 자료 삭제
for i in range(10):
    element = stack[top]
    top -= 1
    print(element, end=",")
print()

print(stack[top], top)
# 뭔가 남아있어도 우리는 이 스택이 이제 비었다고 판단 왜? top이 -1이 이니까
print(stack)