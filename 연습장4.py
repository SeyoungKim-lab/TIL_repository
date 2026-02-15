T = int(input())

for tc in range(1, 1+T):
    # 만들 행렬의 크기
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    
    def pascal(i,j):

        if i == N :
            return

        if i == j or j ==0:
            arr[i][j] = 1
            
        
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            

        print(arr[i][j], end=" ")

        if i ==j:
            print()
            pascal(i+1, 0)
        else:
            pascal(i, j+1)
    
    print(f"#{tc}")
    pascal(0,0)

            

        