class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    # Calculate value/weight ratio and sort items by it
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity == 0:
            break

        if item.weight <= capacity:
            # Take whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take fraction of item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0

    return total_value

# Example data
items = [
    Item(10, 3),
    Item(15, 3),
    Item(10, 2),
    Item(10, 5),
    Item(8, 1)
]
capacity = 50

max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in the knapsack: {max_value}")