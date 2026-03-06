import copy
# import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
#N : 지도의 새로길이
#M : 지도의 가로길이
N, M = map(int, input().split())

JIDO = [list(map(int, input().split())) for _ in range(N)]

# 1. 문제상황
# 빈칸(0)에 벽(1)을 3개세우는데,
# 어디다 세워야 바이러스(2)가 최소로 퍼지는가?
# 그때 빈칸의 갯수.

# 2. 알고리즘/자료구조
# N,M은 3에서8사이 이므로, N*M 해봤자 최대 64.
# 벽 3개를 모든 곳에 다 세워본다해도 복잡도가 그리 크지 않을것으로예상.

# 벽3개를 가능한 모든 곳에 세워보고, 2에서의 BFS탐색을 채택.
# 2의위치를 찾아서 list에 넣어둔다.
# 0의 위치도 찾아서 lst에 넣어둔다.
# 조합: 재귀를 통해 3개의벽을 랜덤하게 다 세워본다.
#     : 세우는 경우들에 대해(종료return하기직전에) BFS탐색을 진행한다. 
#     : BFS를 하기전 지도의 deepcopy본을 만들어 거기서 진행한다.
#     : 카피본에서 탐색하고 바이러스를 다채워주고,
#     : 0의 개수를 센다. 그리고 최댓값 갱신
virus_list = []
def find_virus():
    for i in range(N):
        for j in range(M):
            if JIDO[i][j] == 2:
                virus_list.append((i,j))
find_virus()
count_2 = len(virus_list)

empty_list = []
def find_empty():
    for i in range(N):
        for j in range(M):
            if JIDO[i][j] == 0:
                empty_list.append((i,j))
find_empty()
count_0 = len(empty_list)


def count_safe(temp):
    counts = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                counts += 1
    return counts

max_v = 0   # 0의 최대개수
def make_wall(start,depth):
    global max_v
    if depth == 3:
        temp = copy.deepcopy(JIDO)
        bfs(temp)
        cnt = count_safe(temp)
        if max_v < cnt:
            max_v = cnt
        return
    
    for i in range(start, count_0):
        x, y = empty_list[i]
        JIDO[x][y] = 1  # 벽세우기
        make_wall(i+1, depth+1)
        JIDO[x][y] = 0  # 벽지우기

def bfs(temp):
    #델타탐색
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    #큐
    q = deque(virus_list)

        
    while q:
        vi, vj = q.popleft()   #현위치
        
        for d in range(4):
            wi = vi + di[d]
            wj = vj + dj[d]
            if 0<=wi<N and 0<=wj<M and temp[wi][wj] == 0:
                q.append((wi,wj))
                temp[wi][wj] = 2

make_wall(0,0)
print(max_v)


        
        



