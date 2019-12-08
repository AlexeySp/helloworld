def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        sup = arr[0]
        less = []
        greater = []
        for element in arr[1:]:
            if element < sup:
                less.append(element)
            else:
                greater.append(element)
        return quickSort(less) + [sup] + quickSort(greater)

print(quickSort([10, 12,2,12,1,2,3,44,4,1,1]))