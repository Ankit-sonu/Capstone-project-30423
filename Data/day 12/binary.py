def binarysearch(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        elif array[mid] > key:
            high = mid - 1
    return -1

if __name__ == '__main__':
    array = [2,4,6, 8,11,15,17,19]
    key = 100

    result = binarysearch(array, key)
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found")