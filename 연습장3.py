
A = [1,2,3,4]

for i in range(1<<4):
    subset = []
    for j in range(4):
        if i & (1<<j):
            
            subset.append(A[j])
        
    print(subset)