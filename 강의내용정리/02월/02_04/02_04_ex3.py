arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
N =3 #행 크기
M =4 #열 크기
for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()
for row in arr:
    print(*row)