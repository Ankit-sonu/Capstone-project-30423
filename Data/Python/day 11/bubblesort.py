
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        isswapped = False
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                isswapped = True

        if not isswapped:
            break

def linear_search(list,key):
    isFound = False
    n = len(list)
    for i in range(n):
        if list[i] == key:
            isFound = True
            break

    if isFound :
        print("The value is found")
    else:
        print("The value not found")


if __name__ == '__main__':
    data = [8,16,19,15,2,17,4,11]
    #bubble_sort(data)
    #print(data)
    linear_search(data,1)