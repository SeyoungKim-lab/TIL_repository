# def sequential_search(a, n, key):
#     for i in range(n):
#         if a[i] == key:
#             return i
#     return -1

def sequential_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
        if i < n :
            return i
        else:
            return -1
        
print(sequential_search([1,2,3], 3, 2))

# 이건 원하는 키값이 없을때 끝까지 순회함