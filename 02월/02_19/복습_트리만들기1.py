def postorder(t):
    # t번 노드가 숫자면 실수로 바꿔서 리턴한다. (피연산자로 사용 가능)
    if type(node[t]) is int:
        return node[t]
    # t번 노드가 연산자면 계산
    else:
        # t번 노드의 왼쪽으로 가서 숫자 얻어오기
        left = postorder(cleft[t])
        # t번 노드의 오른쪽으로 가서 숫자 얻어오기
        right = postorder(cright[t])

        ##########################
        # t번 노드에 있는 연산자의 종류에 따라 계산해주기
        if node[t] == "+":
            node[t] = left + right
        if node[t] == "-":
            node[t] = left - right
        if node[t] == "*":
            node[t] = left * right
        if node[t] == "/":
            node[t] = left / right
        # 계산하고 이 계산결과를 또 부모노드가 피연산자로 사용할 수 있도록 리턴
        return node[t]

T = 10

for tc in range(1, T + 1):
    N = int(input())

    # cleft[p] => p번 노드의 왼쪽 자식 노드 번호
    # cright[p] => p번 노드의 오른쪽 자식 노드 번호
    cleft = [0] * (N + 1)
    cright = [0] * (N + 1)

    # 피연산자나, 연산자를 저장할 배열
    # node[i] => i번 노드에 저장된 연산자 혹은 피연산자, 완전 이진 트리가 아님에 주의
    node = [0] * (N + 1)

    for k in range(N):
        lst = input().split()
        if len(lst) == 4:   # 입력값이 4개면
            node_num = int(lst[0])
            op = lst[1]
            l = int(lst[2])
            r = int(lst[3])
            node[node_num] = op
            cleft[node_num] = l
            cright[node_num] = r
        else:   # 입력값이 2개면
            node_num = int(lst[0])
            node[node_num] = int(lst[1])




    answer = int(postorder(1))
    print(f"#{tc} {answer}")