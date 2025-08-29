class Dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Dnode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Dnode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        print("Doubly Linked List in Forward Direction:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        # Go to last node
        while temp.next:
            temp = temp.next
        print("Doubly Linked List in Backward Direction:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Found data '{key}' in the list.")
                return temp
            temp = temp.next
        print(f"Data '{key}' not found in the list.")
        return None

    def delete_data(self, key):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        # if head node holds the key
        if temp.data == key:
            if temp.next:
                temp.next.prev = None
            self.head = temp.next
            return
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            print("Node or data not found")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Dnode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("Circular list is empty")
            return
        print("Circular Doubly Linked List:")
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def search(self, key):
        if not self.head:
            print("List is empty")
            return None
        temp = self.head
        while True:
            if temp.data == key:
                print(f"Found data '{key}' in the circular list.")
                return temp
            temp = temp.next
            if temp == self.head:
                break
        print(f"Data '{key}' not found in the circular list.")
        return None

    def delete(self, key):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while True:
            if curr.data == key:
                if curr.next == curr:
                    self.head = None
                    return
                if curr == self.head:
                    self.head.prev.next = curr.next
                    curr.next.prev = self.head.prev
                    self.head = curr.next
                    return
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return
            curr = curr.next
            if curr == self.head:
                break
        print("Node with data", key, "not found")

if __name__ == "__main__":
    print("\nDOUBLY LINKED LIST")
    dlist = DoubleLinkedList()
    dlist.insert_at_beginning("Python")
    dlist.insert_at_end("Java")
    dlist.insert_at_end("DevOps")
    dlist.insert_at_end("Dotnet")
    dlist.display_forward()
    dlist.display_backward()
    dlist.search("Java")
    dlist.delete_data("Dotnet")
    dlist.display_forward()

    print("\n CIRCULAR DOUBLY LINKED LIST")
    cdlist = CircularDoublyLinkedList()
    cdlist.insert_at_end("C")
    cdlist.insert_at_end("C++")
    cdlist.insert_at_end("Python")
    cdlist.insert_at_end("Java")
    cdlist.display()
    cdlist.search("Python")
    cdlist.delete("C++")
    cdlist.display()
