arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 1번노드의 왼쪽자식이 2번, 1번노드의 오른쪽자식이 3번 이런식으로.
                                #          1
                                #        2     3
                                #       4  5     6
                                #      7  8 9  10  11
                                #    12            13
# 부모를 인덱스로하고, 왼쪽자식과 오른쪽자식 리스트를 만들자
cleft = [0] * 14    # 0번 부모는 깍두기
cright = [0] * 14
# 자식배열에 부모자식관계를 입력하자
for i in range(0,len(arr),2):
    parent = arr[i]
    child = arr[i+1]

    if cleft[parent] == 0:  # 왼쪽자식이 없으면
        cleft[parent] = child   # 왼쪽자식으로 넣고
    else:   # 왼쪽자식이 있으면
        cright[parent] = child  # 오른쪽자식으로 넣자

print(f"왼쪽자식배열:{cleft} 오른쪽자식배열:{cright}")

# 후위순회
def postorder(node):
    
    if node:
        postorder(cleft[node])
        postorder(cright[node])
        print(node, end = ' ')

postorder(1)