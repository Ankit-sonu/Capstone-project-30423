
def quicksort(array,low,high):
    if low < high:
        mid = (low+high)//2
        pivot = array[mid]

        array[mid],array[high] = array[high],array[mid]

        #Partitiong
        i = low -1
        for j in range(low,high):
            if array[j] < pivot:
                i = i+1
                array[i],array[j] = array[j],array[i]
        i+=1
        array[i],array[high] = array[high],array[i]
        quicksort(array,low,i-1)
        quicksort(array,i+1,high)
if __name__ == '__main__':
    data = [8,16,19,15,2,17,4,11]
    quicksort(data,0,7)
    print("Arrays after sorted")
    print(data)
    
