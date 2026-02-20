T = int(input())
 
for tc in range(1,T+1):
    
    N = int(input())
    lst = list(map(int, input().split()))   # 최소힙의 값들
    heap = [0] * (N+1)  # 최소힙으로 사용할 배열
    last = 0    # 마지막에 원소를 넣은 자리
    
    def enq(i):
        global last
        
        last += 1   
        heap[last] = i  
        
        
        
    