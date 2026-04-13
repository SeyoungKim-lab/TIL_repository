import sys
sys.stdin = open("dfs_input.txt", "r")

T = 10

def DFS(now_node):
        global flag
        # 종료조건
        if now_node == 99:
            flag = 1
            return
        
        # 탐색(재귀)
        for next_node in edges[now_node]:
            visited[next_node] = 1
            DFS(next_node)
            visited[next_node] = 0

for tc in range(1, 1+T):

    tc, E = map(int, input().split())

    E_lst = list(map(int, input().split()))
    # 인접리스트
    edges = [[] for _ in range(100)]
    # 두개씩 끊어 인접리스트 완성
    for i in range(0,len(E_lst),2):
        start, end = E_lst[i], E_lst[i+1]
        edges[start].append(end)

    # 방문배열 만들기
    visited = [0] * 100
    # 종료지점에 도착했을때 1로 변경
    flag = 0
    
    # 시작지점 방문 체크
    visited[0] = 1
    DFS(0)
    # 시작지점 방문 해제
    visited[0] = 0

    print(f"#{tc} {flag}")