from math import sqrt

def jump_search(data,key):
    n = len(data)
    step = int(sqrt(n))
    prev = 0

    while prev < n and data[min(step,n) - 1 ] < key:
        prev = step
        step += int(sqrt(n))
        if prev >=n:
            return -1
    for i in range(prev, min(step,n)):
        if data[i] == key:
            return i

    return -1
if __name__ == '__main__':
    data = [5,10,15,20,25,30,35,40,45,50]
    key = 100
    result = jump_search(data,key)
    if result!=-1:
        print(f"Element found at {result}")
    else:
        print("Element not found")