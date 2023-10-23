class Queue:
    def __init__(self):
        self.internal_array = [None]*5
        self.front = 0
        self.back = 0
        self.length = 5
    
    def __str__(self):
        return f"{self.internal_array}\nFront: {self.front} | Back: {self.back}"
    
    def add(self, data):
        if self.internal_array[self.back] == None:
            self.internal_array[self.back] = data
            self.back += 1
        else: print("ERROR queue full")

        if self.back == self.length: self.back = 0

    def remove(self):
        if self.internal_array[self.front] != None:
            rem_element = self.internal_array[self.front]
            self.internal_array[self.front] = None
            self.front += 1
            return rem_element
        else: print("ERROR queue empty")

        if self.front == self.length: self.front = 0


def main():
    test_queue = Queue()
    test_queue.add("fish")
    test_queue.add("penguins")
    test_queue.add("parrots")
    print(test_queue)
    print(test_queue.remove())
    print(test_queue.remove())
    print(test_queue)
    test_queue.add("owls")
    test_queue.add("mice")
    test_queue.add("cats")
    print(test_queue)


if __name__ == "__main__":
    main()
