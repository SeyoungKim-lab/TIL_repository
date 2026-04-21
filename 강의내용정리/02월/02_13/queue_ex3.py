'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s,V):   # 시작정점s , 마지막정점V
    visited = [0]*(V+1)   # visited 생성
    q = []              # 큐 생성
                        # 시작점 인큐
    visited[s] = 1      # 인큐표시
    while q:            # 큐에 남은 정점이 있으면
        t = q.pop(0)            # 디큐해서 t에 저장
        print(t)                # 디큐한 정점 방문
        for w in adj_list[t]:    # t에 인접하고 아직 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)     # w 인큐
                visited[w] = visited[t] + 1 # w 인큐 표시

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트  i행에는 i번 정점에 인접한 정점 번호
adj_list = [[] for _ in range(V+1)] #V번행까지 비어있는 행 준비
for i in range(E):
    v1, v2 = arr[i*2] , arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v2) # 방향이 없는경우
bfs(1, V)