def sequential_search2(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:  # 이 부분은 리스트의 모든 요소보다 key가 작을때 -1을 출력
            return -1 
    return -1 # 여기까지 왔다는 것은 리턴되지 않았다 => 즉, 인덱스의 모든 요소보다 key가 더 크다.

# def sequential_search2(a, n, key):
#     i = 0
#     while i < n and a[i] < key:
#         i += 1
#     if i < n and a[i] == key:
#         return i
#     else:
#         return -1
    
