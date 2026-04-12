import sys
sys.stdin = open("mst_input.txt", "r")

# import heapq
from heapq import heappush, heappop 

# 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# --> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다
def prim(start_node):
         # (가중치, 노드) 형태로 시작점을 담은상태로 큐생성
                  # visited 와 동일하다 - MST 생성
                   # 최소 비용 변수 생성
    # while문 시작
    
        # 힙팝을 해서 현가중치,현노드
        
        # 이미 방문한 노드라면 continue
        
            
        
        # 현재 노드에서 해야할 액션 => MST포함체크와 누적합추가
            # queue 에서 pop 될 때 MST 에 포함되는 게 확정!
        
            # 누적합 추가
        


        # 연결된 노드를 탐색(탐색에서 할 액션은 큐에 넣는 것 한가지뿐)
                
            # 이미 방문했으면 continue
            
                
            # 탐색노드들을 푸시
            
    # 최소비용을 리턴하기
    



# V,E 입력받기

# 인접 리스트

# E줄 입력받아 인접리스트 완성하기(무향)

        
    
    

# 출발 정점과 함께 시작
# 출발 정점을 바꾸어도, 최소비용은 똑같다
# 단, 그래프가 다르게 나올수는 있다.



print(f'최소 비용 = {result}')
