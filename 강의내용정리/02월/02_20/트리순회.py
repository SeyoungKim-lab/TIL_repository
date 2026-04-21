


# 트리 노드 수
N = int(input())
# 트리 정보 한줄
tree = list(map(int, input().split()))
# 한줄에서 두개씩 잘라서 부모 / 자식 노드 트리 만들기

cleft = [0] * (N+1)
cright = [0] * (N+1)

# 두개씩 쪼개야 하는 횟수는 N-1
for i in range(N-1):
    # 앞이 부모 번호
    p = tree[i*2]
    # 뒤가 자식 번호
    c = tree[i*2 +1]
    
    # p번 노드의 왼쪽자식 있는지 체크
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c
        
# 1. 전위순회
def preorder(t):
    # t번 노드가 존재하면
    if t:
        # t번 노드에서 처리해야 할일
        print(t, end=" ")
        # t번 노드의 왼쪽
        preorder(cleft[t])
        # t번 노드의 오른쪽
        preorder(cright[t])
# 2. 중위순회
def inorder(t):
    if t:
        # t번 노드의 왼쪽
        inorder(cleft[t])
        # t번 노드에서 처리해야 할일
        print(t, end=" ")
        # t번 노드의 오른쪽
        inorder(cright[t])

# 3. 후위순회
def postorder(t):
    if t:
        # t번 노드의 왼쪽
        postorder(cleft[t])
        # t번 노드의 오른쪽
        postorder(cright[t])
        # t번 노드에서 처리해야 할일
        print(t, end=" ")
