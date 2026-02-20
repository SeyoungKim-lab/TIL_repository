T = int(input())

for tc in range(1,1+T):
    # E : 간선의 개수
    # N : 시작노드번호
    E, N = map(int, input().split())
    
    
    cleft = [0] * (E+2) 
    cright = [0] * (E+2)
    
    edges = list(map(int, input().split()))
    
    # 간선의 개수만큼 잘라냄
    for i in range(E):
        # 부모 노드번호: 짝수
        p = edges[i*2]
        # 자식 노드번호: 홀수
        c = edges[i*2 +1]
        
        # p번 노드의 왼쪽자식이 없으면 왼쪽부터
        if cleft[p] ==0 :
            cleft[p] = c
        # 있으면 오른쪽
        else:
            cright[p] = c
            
    # 문제에서 원하는 답 = N번 노드에서 순회 시작시 노드의 개수
    count = 0
    
    # t를 루트로 하는 서브트리 전위순회
    def preorder(t):
        global count
        # t번 노드가 존재하면
        if t != 0:
        # t번 처리
            count += 1
        # t번 왼쪽 서브트리 전위순회
            preorder(cleft[t])
        # t번 오른쪽 서브트리 전위순회
            preorder(cright[t])
    preorder(N)
    print(f"#{tc} {count}")