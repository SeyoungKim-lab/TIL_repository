def f(i, N):
    if i == N:
        return
    else:
        f(i+1, N)

f(0,1000)