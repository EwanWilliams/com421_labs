
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"{self.data}"
    
    def link(self, link_node):
        self.next = link_node
        link_node.prev = self


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        new_node = Node(data)
        if self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
    
    def get(self, index):
        current_node = self.first
        for i in range(index):
            if current_node.next == None:
                return "ERROR given index is outside the bounds of the current list"
            else:
                current_node = current_node.next
        return current_node
    
    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.first

        for i in range(index):
            if current_node.next == None:
                return "ERROR given index is outside the bounds of the current list"
            else:
                current_node = current_node.next
        
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev = new_node
        current_node = new_node.prev
        if current_node == None:
            self.first = new_node
        else:
            current_node.next = new_node
    
    def display(self):
        current_node = self.first
        while 1:
            print(f"{current_node} ", end="")
            if current_node.next == None:
                print()
                break
            current_node = current_node.next
        
        

def main():
    test_list = LinkedList()
    test_list.add("Dan")
    test_list.add("Matt")
    test_list.add("Elliott")

    print(test_list.get(2))
    print(test_list.get(5))

    test_list.display()
    test_list.insert("Ewan", 1)
    test_list.display()



if __name__ == "__main__":
    main()