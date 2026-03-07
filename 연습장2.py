from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
 
 
N = int(input())

village = [list(map(int,input())) for _ in range(N)]

# 문제이해.
# 마을에 있는 단지들에 번호를 붙이고,
# 단지의 수를 출력하고,
# 그 단지 내에 있는 집의 개수를 단지별로 오름차순 정렬하여라.

# 알고리즘/자료구조
# cnt_estate cnt_home 변수두개만든다. sub_list 리스트하나만든다.
# for문으로 행우선순회하며, 1의 위치를 찾는다.
# 찾으면 cnt_estate 에 1을 더한다.

# 그 위치를 시작점으로 하여 bfs탐색을 한다.
# bfs탐색은 함수로 따로 만들어보자.
# 들린 곳은 visited처리 대신, cnt_estate 으로 바꾸자. 
# 들릴때마다 cnt_home에 1을더한다.

# 한 단지에대해 bfs가 끝나면, sub_list에 cnt_home을 append한다.

# 그리고 마지막 cnt_estate 값에서 1을 빼면 그것이 단지의 수이고,
# sub_list 를 sort 하여 오름차순정렬한다.
# cnt_estate-1 을 출력하고, sub_list를 for문순회하며 출력한다.

cnt_estate = 0
sub_list = []

def bfs(i,j):
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    q = deque([(i,j)])
    cnt_home = 1
    village[i][j] = 0
    while q:
        ni,nj = q.popleft()
        for d in range(4):
            wi = ni + di[d]
            wj = nj + dj[d]
            if 0<=wi<N and 0<=wj<N and village[wi][wj]==1:
                q.append((wi,wj))
                village[wi][wj] = 0
                cnt_home += 1
    return cnt_home

for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            cnt_estate+=1
            sub_list.append(bfs(i,j))

sub_list.sort()

print(cnt_estate)
for i in sub_list:
    print(i)
            


