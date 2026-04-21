#     0 1 2 3   row(=깊이)
# 0               0 
# 1               1
# 2               2
# 3               3

# 각 행에 한개씩 놓는데, 같은 열에는 둘 수 없게 구현해보기

def Nqueen(row):
    global cnt
    # 1.종료조건
    if row == N:
        cnt += 1
        return
    # 2. 재귀호출
    for i in range(N):  # i: 열번호를 의미
        if visited[i]:
            continue    # 이미 방문한곳이면 그 열은 패스해라.
        visited[i] = 1
        path.append(i)
        Nqueen(row+1)
        path.pop()
        visited[i] = 0

N = 4
visited = [0]*N         # 열에 대한 visited 리스트        
path = []        
cnt = 0
Nqueen(0)
print(f"경우의수={cnt}")