from dnode import Dnode

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

    def insert_before(self, target, data):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp is None:
            print(f"Target '{target}' not found")
            return
        new_node = Dnode(data)
        prev_node = temp.prev
        new_node.next = temp
        new_node.prev = prev_node
        temp.prev = new_node
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node
        print(f"Inserted '{data}' before '{target}'")

    def insert_after(self, target, data):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp is None:
            print(f"Target '{target}' not found")
            return
        new_node = Dnode(data)
        next_node = temp.next
        new_node.prev = temp
        new_node.next = next_node
        temp.next = new_node
        if next_node:
            next_node.prev = new_node
        print(f"Inserted '{data}' after '{target}'")

    def display_forward(self):
        temp = self.head
        print("List forward:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")



def main():
    dlist = DoubleLinkedList()
    print("Initialize list by inserting elements at end.")
    n = int(input("How many initial elements to insert? "))
    for _ in range(n):
        elem = input("Enter element: ")
        dlist.insert_at_end(elem)

    while True:
        dlist.display_forward()
        print("\nChoose operation:")
        print("1. Insert before")
        print("2. Insert after")
        print("3. Exit")
        choice = input("Enter choice [1-3]: ")

        if choice == "1":
            target = input("Enter target element to insert before: ")
            data = input("Enter new element to insert: ")
            dlist.insert_before(target, data)
        elif choice == "2":
            target = input("Enter target element to insert after: ")
            data = input("Enter new element to insert: ")
            dlist.insert_after(target, data)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()