from treenode import TreeNode

class BinaryTreeOperations:
    def insert(self,data,root):
        new_node = TreeNode(data)
        current = root
        while True:
            direction = input("Insert direction:(l-left and r - right) ")
            if direction == "l":
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            elif direction == "r":
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            else:
                print("Invalid direction")

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.inorder(root.left)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data, end=' ')

    def search(self,root,key):
        if root is None:
            print("No Elements were in the tree")
            return False
        if root.data == key:
            return True
        else:
            return self.search(root.left,key) or self.search(root.right,key)


    def get_deep_node(self,root):
        if not root:
            return None
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return current

    def delete_deepest_node(self, root,d_node):
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current is d_node:
                    return None
            if current.left:
                if current.left is d_node:
                    current.left = None
                    return
                else:
                    queue.append(current.left)
            if current.right:
                if current.right is d_node:
                    current.right = None
                    return
                else:
                    queue.append(current.right)


    def delete_node(self,root,value):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == value:
                return None
            else:
                return root
        key_node = None
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current.data == value:
                key_node = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        if key_node:
            d_node= self.get_deep_node(root)
            key_node.data = d_node.data
            self.delete_deepest_node(root,d_node)
            print(f"deleted with node value {key}")
        else:
            print("Value not found in tree to delete")


if __name__ == '__main__':
    tree = BinaryTreeOperations()
    root = TreeNode(10)

    while True:
        choice = input("Do you want add more nodes (y/n)").lower()
        if choice == "y":
            data = input("Insert data")
            tree.insert(data,root)
        else:
            break

    print("In Order Traversal is :\n")
    tree.inorder(root)

    print("In Post Order Traversal is :\n")
    tree.postorder(root)

    print("In Pre Order Traversal is :\n")
    tree.preorder(root)

    key = input("Insert key to search  ")
    if tree.search(root,key):
        print(f"The {key} is found in the tree")
    else:
        print(f"The {key} is not in the tree")

    print("Enter the value to delete from tree")
    ch = input("Enter the value to delete: ")
    tree.delete_node(root,ch)

    print("In Pre Order Traversal is :\n")
    tree.preorder(root)