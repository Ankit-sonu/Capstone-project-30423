class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return "Stack is Empty"

    def display(self):
        return self.stack[::-1]

    def isEmpty(self):
        return len(self.stack) == 0




if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.display())
    stack.pop()
    print(stack.display())
    print(stack.peek())
    print(stack.display())
    stack.push(10)
    print(stack.display())
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()