from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def insert(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print("Data Inserted in Queue")

    def remove(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Elements in Queue are : ")
            temp = self.front
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

    @classmethod
    def from_list(cls, data_list):
        queue = cls()
        for item in data_list:
            queue.insert(item)
        return queue

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    q = Queue.from_list(l)
    q.display()
    q.remove()
    q.display()
