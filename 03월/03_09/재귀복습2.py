N, Type = map(int, input().split())

if Type == 2:
    def recur(idx):
        if idx == N:
            print(*path)
            return
        
        for i in range(1,7):
            if visited[i]:
                continue
            visited[i] = 1
            path.append(i)
            recur(idx+1)
            path.pop()
            visited[i] = 0

    visited = [0]*7
    path = []
    recur(0)

elif Type == 1:
    def recur(idx):
        if idx == N:
            print(*path)
            return
        
        for i in range(1,7):
            
            path.append(i)
            recur(idx+1)
            path.pop()

    path = []
    recur(0)