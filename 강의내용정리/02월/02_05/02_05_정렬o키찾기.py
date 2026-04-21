def sequential_search2(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:  # 이 부분은 리스트의 모든 요소보다 key가 작을때 -1을 출력
            return -1 
        # for문에는 key가 더 큰 경우는 들어있지 않음. 즉, key가 더 크면 for문을 계속순회. 같으면 출력이고, 찾는 키가 없을때는 
        # 밑의 예시처럼 5를 만나는 순간 elif에 걸림. 그러면 없다는거니까 -1을 반환. 근데 key가 7 이런거면은 for문을 다돌아버리고 밑의 return을 만나 -1을 반환.
        # 정리하면
        # 1. 정렬범위 내에 키가 있으면 그 인덱스 리턴.
        # 키가 없는경우 2가지
        # 2. key가 정렬 범위 내부 빈 공간에 있는경우 또는 key가 첫 원소보다도 작은경우 => elif를 만나 -1 리턴
        # 3. key가 마지막원소보다도 큰 경우 => 마지막 리턴을 만나 -1 반환.
    return -1 # 여기까지 왔다는 것은 리턴되지 않았다 => 즉, 인덱스의 모든 요소보다 key가 더 크다.

# [1,2,3,5,6]
# key = 4




# def sequential_search2(a, n, key):
#     i = 0
#     while i < n and a[i] < key:
#         i += 1
#     if i < n and a[i] == key:
#         return i
#     else:
#         return -1
    
