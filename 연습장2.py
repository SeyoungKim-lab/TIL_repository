from heapq import heappop, heappush
import sys
sys.stdin = open("input.txt","r")

T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    def prim(start_node):
        pq = [(0,start_node)]
        MST = [0] * (V+1)
        min_weight = 0

        while pq:
            weight, node = heappop(pq)

            if MST[node]:
                continue

            MST[node] = 1
            min_weight += weight

            for next_weight, next_node in graph[node]:
                if MST[next_node]:
                    continue

                heappush(pq, (next_weight, next_node))
        
        return min_weight

    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    
    result = prim(0)

    print(f"#{tc} {result}")