# 파이썬에서 리스트 메서드 사용해서 스택

# 스택 초기화(선언)
# 내가 빈리스트를 스택으로 사용하겠다.
stack = []

# 스택에 자료를 추가하는 방법
for i in range(10):
    stack.append(i)

print(stack)

# # 스택에서 자료를 삭제하는 방법
# # 자료를 삭제하면 ==> 가장 최근에 저장한 자료가 튀어나온다
# for i in range(10):
#     element = stack.pop()
#     print(element, end=",")
# print()

# 스택안에 몇개가 있는지 모른다.
# 근데 다 꺼내서 확인하고 싶다면 어떻게 ??
if stack:
    print("뭔가있어")

while stack:
    element = stack.pop()
    print(element, end=",")
print()

print(stack)