lst = [1,2,3,4,5]
N = 5

# idx : idx번 원소의 자리를 교환하겠다
def make_perm(idx):

    # 1. 종료조건
    if idx == N:
        print(lst)
        return

    # 2. 재귀호출
    # idx번 원소와 다른위치에 있느 원소를 하나 정하고
    # 자리를 바꾼다. 다른위치(j)의 조건 idx보다 작으면 안된다.
    for j in range(idx,N):
        # idx번 원소와 j번 원소 자리를 바꾸겠다.
        lst[idx], lst[j] = lst[j] , lst[idx]
        make_perm(idx+1)
        # 자리 바꿨던 일을 없던일로 하고 다른애랑 바꿔야 된다.
        lst[idx], lst[j] = lst[j] , lst[idx]

make_perm(0)