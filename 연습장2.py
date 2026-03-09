# 주사위 3개를 던져서 합이 10이하인 케이스의 수

# 상태공간트리
# 주사위3개 => depth 3
# branch 수: 1~6숫자 -> 6

result = 0

def recur(cnt, total):
    global result
    
    if total > 10:
        return
    
    if cnt == 3:
        # 경로의 합이 10 이하라면

        result += 1
        return
    
    for num in range(1,7):
        recur(cnt + 1, total + num)
        
recur(0, 0)
print(result)