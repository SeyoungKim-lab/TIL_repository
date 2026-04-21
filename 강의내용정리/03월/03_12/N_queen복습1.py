#     0 1 2 3   row(=깊이)
# 0               0 
# 1               1
# 2               2
# 3               3

# 각 행에 한개씩 놓는 경우의 수 구현해보기

def Nqueen(row):
    global cnt
    # 1.종료조건
    if row == 4:
        cnt += 1
        return
    # 2. 재귀호출
    for i in range(4):
        path.append(i)
        Nqueen(row+1)
        path.pop()
        
path = []        
cnt = 0
Nqueen(0)
print(f"경우의수={cnt}")