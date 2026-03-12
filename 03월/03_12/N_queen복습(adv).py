#     0 1 2 3   
# 0     c                
# 1     c             
# 2   c           
# 3       c     
       
# visited[0,1,2,3] == 0    => 디폴트로는 0열이 다 채워져있다고 시작
# 본인 위쪽만 바라보며 겹치지 않는 곳에 둔다.
# 본인 위쪽을 체크하기전에 퀸을 그위치에 둬본다.(그래야 올바른체크가능)
# 체크함수: 세로와 대각선을 체크

def check(row):
    for pre_row in range(row):
        # 세로 확인부분
        if visited[row] == visited[pre_row]:
            return False
        # 대각선 확인부분
        if abs(row - pre_row) == abs(visited[row] - visited[pre_row]):   # 행차이=열차이 이면
            return False
    return True
        
        
def recur(row):
    global cnt
    # 종료조건
    if row == N:
        cnt += 1
        return
    # 재귀부분
    for col in range(N):
        visited[row] = col # (row,col)을 방문했다 라고 가정
        if not check(row):  # 그곳에 둘 수 다음 열로 넘겨라
            continue
        recur(row+1)    # 둘 수 있다면 두고 다음 행으로.

N = 8
visited = [0] * N
cnt = 0

recur(0)
print(f'N = {N} / answer = {cnt}')

