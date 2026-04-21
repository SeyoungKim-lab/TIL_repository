class TreeNode:
    def __init__()
    



# root 노드에서 시작, key값을 가진 노드 찾기
# 어떤 서브트리의 루트 노드
def search(root, key):
    
    # key값과 루트 노드 비교
    if key == root.key:
        return root
    
    # key 값이 더 크다면
    if root.key < key:
        # 내가 찾는 key 값이 루트의 키값보다 크면 오른쪽으로
        return search(root.right, key)
    # key 값이 더 작다면
    if root.key > key:
        return search(root.left, key)
    
def insert(root, key):
    # 트리가 없는상태, 루트노드에 key 를 삽입
    if root is None:
        return TreeNode(key)
    # 루트 노드가 있다면, key 값 탐색후 탐색실패한 위치에 key값을 가진 노드 삽입
    else:
        # 우리가 삽입하려고 하는 key가 루트보다 작은경우
        if key < root.key:
            root.left = insert(root.left, key)
        # 우리가 삽입하려고 하는 key가 루트보다 큰경우
        else:
            root.right = insert(root.right, key)
            
    return root