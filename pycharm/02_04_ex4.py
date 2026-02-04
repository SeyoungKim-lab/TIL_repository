arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
N =3 #행 크기
M =4 #열 크기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(N):
    for j in range(M):
        for d in range(4): # 방향별로
            ni = i + di[d]
            nj = j + dj[d]
        #     for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        #         ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                print(arr[ni][nj])