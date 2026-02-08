N = int(input())
text = [input() for _ in range(N)]
ans = 'NO'
for i in range(N):
    for j in range(N):
        if text[i][j] == 'Z':
            ans = 'YES'
            break # for j
    if ans == 'YES':
        break # for i
print(ans)