from dnode import Dnode

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None


    def insert_at_front(self, data):
        new_node = Dnode(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print("Data inserted at front")

    def insert_at_rear(self, data):
        new_node = Dnode(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        print("Data inserted at rear")

    def delete_at_front(self):
        if self.front is None:
            print("Deque is empty")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        print(f"Element deleted at front: {data}")
        return data

    def delete_at_rear(self):
        if self.rear is None:
            print("Deque is empty")
            return None
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        print(f"Element deleted at rear: {data}")
        return data

    def forward(self):
        temp = self.front
        while temp:
            print(temp.data, end="<-->")
            temp = temp.next
        print()  # for newline

    def backward(self):
        temp = self.rear
        while temp:
            print(temp.data, end="<-->")
            temp = temp.prev
        print()  # for newline

if __name__ == "__main__":
    d = Deque()
    d.insert_at_front("India")
    d.forward()
    d.insert_at_rear("America")
    d.forward()
    print("\nBackward traversal:")
    d.backward()
    d.insert_at_rear("Japan")
    d.insert_at_front("America")
    d.delete_at_front()
    d.forward()
    d.delete_at_rear()
    d.forward()