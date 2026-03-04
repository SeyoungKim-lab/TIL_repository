def dfs(row, total):
    global min_sum
    
    # 가지치기
    if total >= min_sum:
        return
    
    # 모든 행을 다 선택한 경우
    if row == N:
        min_sum = min(min_sum, total)
        return
    
    for col in range(N):
        if not used[col]:   # 아직 사용하지 않은 열이면
            used[col] = True
            dfs(row + 1, total + arr[row][col])
            used[col] = False  # 원상복구


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    used = [False] * N
    min_sum = float('inf')
    
    dfs(0, 0)
    
    print(f"#{tc} {min_sum}")