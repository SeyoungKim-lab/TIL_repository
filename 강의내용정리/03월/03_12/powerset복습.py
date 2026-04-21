# 1   O         X
# 2  O X       O X
# 3 O X O X  O X O X

def powerset(idx, subset, total):
    # 0. 가지치기
    if total > 10:
        return
    # 1. 종료조건
    if idx == N:
        if total == 10:
            print(*subset)
        return
    # 2. 재귀호출
    # 포함하는경우
    powerset(idx+1, subset + [arr[idx]], total + arr[idx])
    # 포함하지 않는경우
    powerset(idx+1, subset, total)
        
        
        
N = 10
arr = [i for i in range(1,N+1)]
powerset(0, [], 0)
