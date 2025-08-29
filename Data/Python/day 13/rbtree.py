class Node:
    def __init__(self, key):
        self.data = key
        self.color = 'RED'
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 'BLACK'
        self.root = self.NULL

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NULL
        new_node.right = self.NULL
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.NULL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fix_insert(new_node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'RED':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 'RED':
                    # Case 1: Recoloring
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: Right Rotate
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: Left Rotate
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 'RED':
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
        self.root.color = 'BLACK'

    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.data}({node.color})", end=" ")
            self.inorder(node.right)

# -------- MAIN ----------
if __name__ == "__main__":
    rbt = RedBlackTree()
    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            rbt.insert(val)
        elif choice == '2':
            print("Inorder traversal (value(color)):")
            rbt.inorder(rbt.root)
            print()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")