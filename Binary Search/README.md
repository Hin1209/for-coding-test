# 이진 탐색(Binary Search)
--- 
앞에서 배운 퀵 정렬처럼 반으로 계속 쪼개어가며 탐색을 하는 방식으로, 정렬이 이미 되어있는 리스트에서만 쓸 수 있다.   
시간 복잡도는 O(logN) 이다.     
~~~ 
재귀 함수로 표현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    else:
        binary_search(array, tartget, mid + 1, end)
~~~
   
~~~
반복문으로 표현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
~~~
