# 마지막 노드 V, 간선의 개수 N
V, N = map(int, input().split())
# 트리의 정보가 한줄 입력으로 들어온다.
tree = list(map(int, input().split()))
# 5 4
# 1 2 1 3 3 4 3 5
# 1-2/1-3/3-4/3-5

# 부모 노드 번호를 인덱스로 저장하는 방법
cleft = [0] * (V +1)
cright = [0] * (V+1)
# cleft[4] = 4번 노드의 왼쪽 자식 번호
# cright[1] = 1번 노드의 오른쪽 자식 번호

# 한줄 입력을 간선 개수만큼 자른다.
for i in range(N):
    # 부모 번호
    p = tree[2*i]
    # 자식 번호
    c = tree[2*i +1]
    
    # p의 자식은 c번이다.
    # 이진트리에서 자식은 왼쪽? 오른쪽?
    
    # 먼저 왼쪽 자식이 있나 확인
    # p번노드의 왼쪽 자식이 없다면
    if cleft[p] == 0:
        # 왼쪽 자식으로 c 넣기
        cleft[p] = c
    # p번노드의 왼쪽자식이 있었다면
    else:
        # 오른쪽 자식으로 c넣기
        cright[p] = c
        
print(cleft)
print(cright)