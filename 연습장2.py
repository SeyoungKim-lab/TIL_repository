import sys
input = sys.stdin.readline

# N : 행의개수
# M : 열의개수
N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

# 문제정리
# (0,0) => (N-1, M-1)까지의 최단경로세기
# (이때, 시작점과 끝점도 포함)
# 최대 1개까지 벽을 부술 수 있다.
# 그래도 안된다면 -1을 출력하기.

# 방법구상
# 행우선순회로 벽을 하나씩 부순 미로들에 대해서
# bfs탐색을 통해 각각의 경우 최단거리를 다 구한다.
# (단, 벽을 구하고 최단거리 구하면 다시 닫아줘야함.)
# 그 최단거리 중에 -1을 제외한 최솟값이 우리가 원하는 답이다.
# 만약 모든 경우에 다 -1 이라면, (즉 최댓값이 -1이라면) -1을출력한다.

si, sj = 0, 0   # 시작점은 0,0
gi, gj = N-1, M-1   # 도착점은 N-1, M-1

# 큐생성
q = []
# 방문기록부
visited = [[0]*M for _ in range(N)]
# 델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]
# 시작위치를 방문기록부에 찍어주기
visited[si][sj] = 1
# 시작위치를 인큐해주기
q.append([si,sj])
# 최솟값저장
min_v = 2500

for i in range(N):
    for j in range(M):
        if maze[i][j] == 1:
            maze[i][j] = 0  # 벽을부쉈다.

            # bfs 탐색
            while q:
                vi,vj = q.pop(0)    # 디큐한것이 현위치

                if vi == N-1 and vj == M-1:
                    break
                
                for d in range(4):
                    wi = vi + di[d]
                    wj = vj + dj[d]
                    # 갈 수 있는 곳이면
                    if 0<=wi<N and 0<=wj<M and not visited[wi][wj] and maze[wi][wj] != 1:
                        q.append([wi,wj])   # 인큐하기
                        visited[wi][wj] = visited[vi][vj] + 1 # 방문도장찍기

            

            # 목적지까지 못갔다면, visited[N-1][M-1]==0 일테고,
            # 목적지까지 갔다면 visited[N-1][M-1]는 다른값일 것임.
            distance = visited[N-1][M-1]

            # 다음 벽을 부수기 전에 모든조건을 초기화
            maze[i][j] = 1
            visited = [[0]*M for _ in range(N)] 
            visited[si][sj] = 1
            q = []
            q.append([si,sj])

            # 만약 distance가 0이라면, 최솟값갱신하지말고 다음벽 부수러가라.
            if distance == 0:
                continue

            # distance가 0이 아닌 경우에 한해 최솟값을 갱신
            if min_v > distance:
                min_v = distance

            
# 만약 distance가 다 0이다. 즉, 목적지까지 못갔다. 라고 하면, 최솟값이 전혀 갱신되지 않았을 것임.
if min_v == 2500:
    answer = -1
else:
    answer = min_v

print(answer)

            
            