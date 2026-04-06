N = 10

# 트리로 집합을 표현
# p[4] 는 4번사람의 부모
p = [0] * (N+1)

# 초기화 연산
def make_set(x):
    p[x] = x

# 대표가 누군지 찾는 연산
# x가 속한 집합의 대표찾기
def find_set(x):
    if x == p[x]:
        return x
    
    return find_set(p[x])

# 두 집합을 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합친다.
# 각 집합의 대표가 필요하다.
def union(x,y):
    # x가 속한 집합의 대표가 누구니
    king_x = find_set(x)
    # y가 속한 집합의 대표가 누구니
    king_y = find_set(y)

    if king_x == king_y:
        return
    
    p[king_y] = king_x

p = [i for i in range(N+1)]
print(p)