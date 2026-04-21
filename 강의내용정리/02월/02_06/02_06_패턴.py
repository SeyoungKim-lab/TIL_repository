def 
    i = j = 0
    cnt = 0
    while i < N
        if t[i] != p[j]: # 다르면
            i = i - j +1 # i-j 비교를 시작했던 위치
            j = 0
        else: #같으면
            i += 1
            j += 1
        if j==M: #패턴을 찾은경우
            cnt += 1
            i = i-j+1
            j = 0
    return cnt