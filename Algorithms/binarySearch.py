def binarySearch(array, value):
    low = 0
    high = len(array) - 1
    mid = int ((high + low) / 2)
    while(True):
        if(array[mid] == value):
            return mid + 1
        elif (array[mid] > value):
            high = mid - 1
            mid = int((high + low) / 2)
        elif (array[mid] < value):
            low = mid + 1
            mid = int((high + low) / 2)
        if (high == low and array[low] != value):
            return None
    

array = [1, 2, 7, 9, 12, 15, 23]
value = 7
print("Value: " + str(value) + " Position: " + str(binarySearch(array, 7)))