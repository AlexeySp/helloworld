def findMaxElementIndex(arr):
    max = 0
    maxIndex = 0
    for idx in range(len(arr)):
        if(arr[idx] >= max):
            max = arr[idx]
            maxIndex = idx
    return maxIndex

def findMinElementIndex(arr):
    min = 0
    minIndex = 0
    for idx in range(len(arr)):
        if(min >= arr[idx]):
            min = arr[idx]
            minIndex = idx
    return minIndex

def  selectionSort(arr, order = 'desc'):
    sortedArr = []
    for _ in range(len(arr)):
        if order.lower() == 'desc':
            sortedArr.append(arr.pop(findMaxElementIndex(arr)))
        elif order.lower() == 'asc':
            sortedArr.append(arr.pop(findMinElementIndex(arr)))
        else:
            print('Order type not found. Default asc')
            sortedArr.append(arr.pop(findMinElementIndex(arr)))
    return sortedArr

print(findMaxElementIndex([1, 5, 7]))
print(findMinElementIndex([1, 5, 7]))
print(selectionSort([5, 3, 2, 1, 123, 4, 17], 'asc'))
