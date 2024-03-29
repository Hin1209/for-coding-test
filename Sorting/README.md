#정렬 알고리즘  
----
* 선택 정렬: 이중 for문을 이용해 자신보다 작은 원소가 나오면 자리를 바꿔주는 정렬(시간 복잡도 N**2)      
~~~
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
~~~
* 삽입 정렬: 이중 for문을 이용. 왼쪽의 원소들과 비교하여 처음으로 자신보다 작은 원소가 나오는 위치에 삽입.(정렬이 많이 되어있을 수록 시간이 적게 소요됨.)     
~~~
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
~~~
* 퀵 정렬:    
(1) 첫번째 원소를 Pivot 으로 설정하고 다음 원소부터 오른쪽으로 가면서 Pivot 보다 큰 원소를, 끝에서부터 왼쪽으로 오면서 Pivot 보다 작은 원소를 찾는다.    
(2) 이 때 큰 원소가 작은 원소보다 오른쪽에 있으면 Pivot과 작은 원소의 위치를 바꾸고 Pivot을 기준으로 왼쪽과 오른쪽의 리스트를 분할하여 (1) 부터 반복하고, 
큰 원소가 작은 원소보다 왼쪽에 있으면 둘이 자리를 바꿔준다.    
(3) 분할한 리스트의 크기가 1이 되면 함수를 종료한다.  
-> 재귀함수 형태로 구현하며, 평균적인 시간 복잡도는 NlogN 이며 최악의 경우에는 N**2 이다.   
~~~
def qsort(start, end, array):
    pl = start
    pr = end
    x = array[(left + right) // 2]

    while pl <= pr:
        while array[pl] < x: pl += 1
        while array[pr] > x: pr -= 1
        if pl <= pr: 
            array[pl], array[pr] = array[pr], array[pl]
            pl += 1
            pr -= 1
    if start < pr: qsort(start, pr, array)
    if end > pl: qsort(pl, right, array)
~~~

* 병합 정렬:
항상 O(n log n)의 시간복잡도를 보장함. but 다른 정렬 알고리즘에 비해 메모리를 많이 사용함 
~~~
def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    merged_array = []
    low = 0
    high = 0
    while low < len(low_array) and high < len(high_array):
        if low_array[low] < high_array[high]:
            merged_array.append(low_array[low])
            low += 1
        else:
            merged_array.append(high_array[high])
            high += 1
    merged_array += low_array[low:]
    merged_array += high_array[high:]
    return merged_array
~~~
   
* 계수 정렬:    
데이터의 크기가 제한되어 있을 때 쓰기 좋음. (데이터의 최댓값)+1 을 크기로 갖는 리스트를 만들어 주고 각 데이터가 나오는 횟수를 새로 만든
리스트에 저장해줌. 이후에 작은 인덱스부터 저장된 횟수만큼 인덱스 값을 원래 리스트에 덮어씌워주면 정렬 완료   
리스트의 크기를 N, 원소의 최댓값을 K라고 했을 때 시간 복잡도는 언제나 (N+K)임. 최댓값이 너무 큰 경우에는 비효율적.   
   
* 정렬 라이브러리:   
파이썬은 기본 라이브러리에서 정렬 라이브러리인 sorted() 함수를 제공한다. 이외에 list 객체의 메소드인 .sort()도 존재하며, 
sort(key = function()) 을 통해 정렬의 기준을 지정해줄수 있다. 보통 lambda 함수를 자주 이용한다.    
정렬 라이브러리는 항상 최악의 경우에도 NlogN 의 시간 복잡도를 보장한다.    
----
