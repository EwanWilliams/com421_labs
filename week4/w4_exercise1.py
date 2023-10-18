class Stack:
    def __init__(self):
        self.internal_array = []
    
    def __str__(self):
        return f"{self.internal_array}"
    

    def push(self, item):
        self.internal_array.append(item)
    
    def pop(self):
        if len(self.internal_array) == 0:
            return "ERROR empty stack"
        else:
            pop_value = self.internal_array[-1]
            del self.internal_array[-1]
            return pop_value
    
    def peek(self):
        if len(self.internal_array) == 0:
            return "ERROR empty stack"
        else:
            return self.internal_array[-1]



def main():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(4)
    stack1.push(9)
    print(stack1)
    print(stack1.pop())
    print(stack1)

    stack2 = Stack()
    stack2.push("Linux")
    stack2.push("Windows")
    stack2.push("Mac OS X")
    print(stack2)
    print(stack2.pop())
    print(stack2)
    print(stack2.peek())
    print(stack2)


if __name__ == "__main__":
    main()