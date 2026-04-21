T = int(input())

for tc in range(1, 1+T):
    # 노드의 개수가 N개인 완전 이진 트리
    N = int(input())
    # 노드의 개수가 N개인 비어있는 트리 만들기
    tree = [0] * (N+1)
    
    # +1할 숫자(노드안에적을숫자)
    num = 1
    
    # 이 비어있는 트리를 중위순회 하면서
    # 만나는 노드에 1씩 증가하는 숫자를 적으면 끝
    def inorder(t):
        global num
        # t번 노드가 존재하는가?
        if t <= N:  # t가 존재하는 노드면
            # t번 노드의 왼쪽 서브 트리순회
            inorder(t*2)
            # t번 노드에 +1한 숫자 쓰기
            tree[t] = num
            print(num, end = '')
            num += 1
            # t번 노드의 오른쪽 서브 트리순회
            inorder(t*2 + 1)
    # 1번 노드에서 중위순회 시작
    inorder(1)     
    print(f"#{tc} {tree[1]} {tree[N//2]}")   
    