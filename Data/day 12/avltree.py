class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Function to get height of node
def get_height(node):
    if not node:
        return 0
    return node.height

# Function to get balance factor
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

# Right rotate
def right_rotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1

    return x

# Left rotate
def left_rotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1

    return y

# Insert into AVL tree
def insert(root, key):
    # Normal BST insert
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Get balance
    balance = get_balance(root)

    # Case 1 - LL
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Case 2 - RR
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Case 3 - LR
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 4 - RL
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# ----------- MAIN PROGRAM -----------

if __name__ == "__main__":
    root = None
    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            key = int(input("Enter value to insert: "))
            root = insert(root, key)
        elif choice == '2':
            print("Inorder traversal:")
            inorder(root)
            print()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")