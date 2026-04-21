N = int(input())
text = [input() for _ in range(N)]

# '#' 개수는?
cnt = 0
for i in range(N):
    for j in range(N):
        if text[i][j] == '#':
            cnt += 1
print(cnt)