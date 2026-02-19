
V = int(input())
arr = list(map(int, input().split()))

E = V - 1       # V = E + 1
# 부모번호를 인덱스로 자식번호를 저장하는 배열
c1 = [0] * (V +1)
c2 = [0] * (V +1)

# 자식번호를 인덱스로 부모번호를 저장하는 배열
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if c1[p] == 0:  # 아직 자식1이 없으면
        c1[p] = c
    else:
        c2[p] = c
    par[c] = p      # 자식을 인덱스로 부모 저장
    
??