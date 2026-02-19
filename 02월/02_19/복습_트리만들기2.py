# 마지막 노드 V, 간선의 개수 N
V, N = map(int, input().split())
# 트리의 정보가 한줄 입력으로 들어온다.
tree = list(map(int, input().split()))

# 자식 번호를 인덱스로 부모 번호를 저장
parent = [0] * (V+1)
# parent[2] = 2번자식의 부모노드번호
# parent[4] = 4번자식의 부모노드번호
# x번 노드의 부모노드번호를 알고싶어요 => parent[x]
for i in range(N):
    # 부모 번호
    p = tree[2*i]
    # 자식 번호
    c = tree[2*i +1]
    
    # c번 노드의 부모노드 번호는 p번이다
    parent[c] = p
    
print(parent)

# 5번 노드의 조상 노드 모두 찾고싶다
child = 5

ancestor = []

while parent[child] != 0:
    # child 의 부모노드가 0이 아니다 => child는 루트노드가 아니다.
    # child 의 부모 위로 한칸 올라가 본다.
    child = parent[child]
    # 이 노드는 부모노드니까 조상목록에 추가
    ancestor.append(child)

# 어느 순간 child 의 부모번호가 0번이 된다.
# == child는 루트 노드다.
root = child
print(root, ancestor)

# 5 4
# 1 2 1 3 3 4 3 5