from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        #new_node.data = data
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("List is Empty")
        else:
            while current:
                print(current.data , end = "->")
                current = current.next

    def search_list(self, key):
        current = self.head
        found=False
        if not current:
            print("List is Empty")
        else:
            while current:
                if current.data == key:
                    found=True
                    break
                current = current.next

        if found:
            print("The key is found ")
        else:
            print("The Key is not found")

    def delete_node(self,key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data!= key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("The key is not found")
            return
        prev.next = temp.next
        temp = None
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning("India")
    linked_list.display()
    print("\n")
    linked_list.insert_at_end("China")
    linked_list.display()
    print("\n")
    linked_list.insert_at_end("Japan")
    linked_list.display()
    print("\n")

    linked_list.insert_at_beginning("America")
    linked_list.display()
    print("\n")

    linked_list.search_list("Australia")

    linked_list.delete_node("Japan")
    linked_list.display()