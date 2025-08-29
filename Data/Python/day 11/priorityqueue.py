from node import Node

class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def insert(self, data):
        newNode = Node(data)
        if self.front is None or data < self.front.data:
            newNode.next = self.front
            self.front = newNode
        else:
            temp = self.front
            while temp.next and temp.next.data <= data:
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
        print(f"Data Inserted in PriorityQueue: {data}")

    def remove(self):
        if self.is_empty():
            print("PriorityQueue is Empty")
            return None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.data

    def display(self):
        if self.is_empty():
            print("PriorityQueue is Empty")
        else:
            print("Elements in PriorityQueue are (in priority order):")
            temp = self.front
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

    @classmethod
    def from_list(cls, data_list):
        pq = cls()
        for item in data_list:
            pq.insert(item)
        return pq

if __name__ == "__main__":
    l = [4, 1, 3, 2]
    pq = PriorityQueue.from_list(l)
    pq.display()

    pq.remove()
    pq.display()