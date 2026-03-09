path = []
N = 7
used = [0]*N

def recur2(cnt):
    if cnt == 3:
        print(*path)
        return
    

    for i in range(1,7):
        
        # used[i] = 1
        path.append(i)
        recur2(cnt+1)
        path.pop()
        
recur2(0)