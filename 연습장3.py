arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
# arr = [11, 45, 23, 81, 28, 34]
# arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
# arr = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]




def hoare_partition1(left, right):
    pivot = arr[left]  
    i = left + 1
    j = right

    while i <= j:  
        while i <= j and arr[i] <= pivot:  
            i += 1

        while i <= j and arr[j] >= pivot:  
            j -= 1

        if i < j:  
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[left], arr[j] = arr[j], arr[left]
    return j




def quick_sort(left, right):    # 넘겨받은 인자가 양끝인덱스가 됨
    if left < right:    # pivot 기준으로 양옆을 자를텐데,
        # 1.양옆에 1개가 남으면 left==right 인거고,
        # 2.왼쪽에 아무것도 없으면(pivot이 제일왼쪽이면) right<left가 되버리고,
        # 3.오른쪽에 아무것도 없으면(pivot이 제일오른쪽이면) right<left가 되버린다.
        # 즉 위의 3가지 경우에 대해서는 더이상 그 구간을 정렬할 필요가 없으므로, 
        # if문에 벗어나서 자동 return되버린다.
        # 즉, 이 재귀함수의 종료조건은 pivot기준으로 짤린구간에 원소가 없거나 한개만 있는 경우이다.

        pivot = hoare_partition1(left, right)
        
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1) # arr의 0번인덱스와 끝번인덱스를 입력
print(arr)
