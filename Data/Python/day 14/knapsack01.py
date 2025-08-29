def knapsack(capacity, n):
    print(f"Kanpsack with capacity = {capacity}, when item {n} is added." )
    if n == 0 or capacity == 0:
        return 0
    elif weights[n-1] > capacity:
        return knapsack(capacity, n-1)
    else:
        include_item = values[n-1] + knapsack(capacity - weights[n-1], n-1)
        exclude_item = knapsack(capacity, n-1)
        return max(include_item, exclude_item)


values = [300,200,400,500]
weights = [2,1,5,3]
capacity = 10
n = len(values)

print("maximum value in knapsack = ", knapsack(capacity, n))