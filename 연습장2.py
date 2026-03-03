T = int(input())

for tc in range(1, 1+T):
    # N: 노드의 개수
    # M: 리프노드의 개수
    # L: 값을 출력할 노드번호
    N, M, L = map(int, input().split())

    # 트리생성
    tree = [0] * (N+1)

    # 리프노드에 값넣기
    for i in range(M):
        num, value = map(int, input().split())
        tree[num] = value
    
    # 후위순회
    def postorder(i):
        if i > N:
            return 0
        # 왼쪽자식호출
        left = postorder(i*2)
        # 오른쪽자식호출
        right = postorder(i*2+1)

        result = tree[i] + left + right
        tree[i] = result
        return result
    postorder(1)
    print(f"#{tc} {tree[L]}")