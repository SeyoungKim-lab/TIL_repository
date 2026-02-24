T = int(input())

for tc in range(1, 1 + T):
    # N: 노드의 개수
    # M: 리프노드의 개수
    # L: 값을 출력할 노드
    N, M, L = map(int, input().split())
    # 노드의 개수가 N개인 비어있는 트리 만들기
    tree = [0] * (N + 1)
    # 리프의개수 M번 입력을 받는다.
    for k in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value



    def postorder(t):   # 후위순회할것임
        if t <= N:  # 현재노드가 tree범위 내에 있으면
            if tree[t] != 0 : # t번노드의 값이 0이 아니면(= t번노드가 리프노드면)
                return tree[t]  # 리프노드에 적혀있는 값을 반환
            # t번 노드의 왼쪽,오른쪽 서브트리 더한값이 number
            left_child = postorder(t * 2)   # 왼쪽자식을 호출
            right_child = postorder(t * 2 + 1)  # 오른쪽자식을 호출
            sum_of = left_child + right_child
            tree[t] = sum_of    # 두 자식값의 합을 현재노드에 입력

            return sum_of
        else:   # 현재노드가 tree범위밖이면(=리프노드의 아랫줄이면)
            return 0    # 0을 반환하라



    # 1번 노드에서 중위순회 시작
    postorder(1)
    print(f"#{tc} {tree[L]}")
