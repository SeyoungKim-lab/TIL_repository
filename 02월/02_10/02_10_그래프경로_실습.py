import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, T+1):
    # V = 정점의개수
    # E = 간선의개수
    V = 100
    TC, E = map(int, input().split())

    # 인접 행렬
    # adj_m[1][2] == 1 => 1번에서 2번가는길 o
    adj_m = [[0] * V for _ in range(V)]

    # 그래프 정보 입력
    # 출발-도착 정점 쌍(간선) 정보가 E개 입력으로 들어온다.
    graph = list(map(int, input().split()))
    for i in range(E):
        s, e = graph[i*2], graph[i*2+1]
        adj_m[s][e] = 1
        # adj_m[e][s] = 1 요건안됨(무향일때사용)
    
    # 테스트케이스 입력 마지막에 출발 정점 번호, 목표 정점 번호
    start, finish = 0, 99

    # start에서 출발하는 DFS 탐색, 탐색중 finish를 만나면 탐색 종료

    # 처음엔 도착 불가능이라고 가정, DFS탐색 중 finish를 만나면 1로
    answer = 0

    #### DFS
    


    visited = [0] * V

    stack = []

    visited[start] = 1

    # 현재 내가 방문하고 있는 정점 번호 v
    v = start

    # 그래프 탐색 시작
    while True:
        if v == finish:
            answer = 1
            break
        # 현재 내가 있는 정점 번호는 v
        # v와 인접한 정점(w)이 있나 없나 확인 => 있다면 이전에 방문했나 안했나 확인
        # 방문 가능하면 방문한다.
        for w in range(V):
            # v와 w가 인접하고, w를 이전에 방문한 적이 없으면 방문한다.
            if adj_m[v][w] and not visited[w]:
                stack.append(v)
                visited[w] = 1
                v = w
                break
        else:
            # 갈 곳이 없다. 이전길로 돌아가기
            if stack:
                # 스택에서 돌아갈곳 꺼내서 현재 위치로 바꾸기
                v = stack.pop()
            else:
                # 스택이 비었다면 돌아갈 곳이 없다. => 모든 정점 탐새 완료
                break # while
    
    



    print(f"#{tc} {answer}")