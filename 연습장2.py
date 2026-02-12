lst = [1,2,3,4,5]
N = 5

def make_set(idx, selected):
    
 
    if idx == N:
        
        for i in range(N):
            if selected[i]:
                print(lst[i], end=" ")
        print()
        return

    
    selected[idx] = 1
    make_set(idx+1, selected)

    
    selected[idx] = 0
    make_set(idx+1, selected)

make_set(0, [0]*N)