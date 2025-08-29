from treenode import TreeNode
class BST:
    def __init__(self):
      self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root


    def search(self,root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)


    def delete(self,root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.findmin(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root


    def findmin(self,root):
        while root.left is not None:
            root = root.left
        return root


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

if __name__ == '__main__':
    bst = BST()
    root = bst.insert(bst.root, 40)
    bst.insert(root, 20)
    bst.insert(root, 10)
    bst.insert(root, 8)
    bst.insert(root, 60)
    bst.insert(root, 50)
    bst.inorder(root)
    key = int(input("Enter search value in tree"))
    found = bst.search(root, key)
    if found:
        print("The data found in tree")
    else:
        print("The data not found in tree")
    root = bst.delete(root, 40)
    bst.inorder(root)