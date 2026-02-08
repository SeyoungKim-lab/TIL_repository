N = int(input())
text = [input() for _ in range(N)]
pat = ['AB', 'CD']
ans = 'NO'
#  AB/CD 패턴찾기
for i in range(N-1): # 패턴 기준 i,j
    for j in range(N-1):
        cnt = 0
        for p in range(2) : #  패턴 내부 인덱스
            for q in range(2):
                if text[i+p][j+q] == pat[p][q]:
                    cnt += 1
        if cnt == 4:
            ans = 'YES'
            # 함수로만들어서 return 'YES' 가 좋긴함
print(ans)


            