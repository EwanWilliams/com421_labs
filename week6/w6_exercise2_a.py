class Hashtable:
    def __init__(self, size):
        self.buckets = [None]*size
        self.size = size
    

    def put(self, key, value):
        insert_index = self.get_hash(key)
        while 1:
            if insert_index > self.size - 1:
                insert_index = 0
            elif self.buckets[insert_index] == None:
                self.buckets[insert_index] = (key, value)
                break
            else:
                insert_index += 1
    

    def get(self, key):
        return_index = self.get_hash(key)
        while 1:
            if (self.buckets[return_index])[0] == key:
                return self.buckets[return_index]
            else:
                return_index += 1


    def get_hash(self, key):
        hash_code = self.primary_hash(key)
        hash_code += hash_code % 17
        return hash_code
    

    def primary_hash(self, key):
        hash_code = 0
        for i in range(len(key)):
            hash_code += ord(key[i])*(31^i)
        
        return hash_code % self.size
    


def main():
    test_table = Hashtable(127)

    test_table.put("cat", "Bobby")
    test_table.put("hashtable", "good")
    test_table.put("geez", "god damn this sucks")
    test_table.put("act", "Not Bobby")
    test_table.put("KC", "Kacey")

    for i in range(len(test_table.buckets)):
        if test_table.buckets[i] == None:
            continue
        print(f"{i}: {test_table.buckets[i]}")
    
    print(test_table.get("cat"))
    print(test_table.get("act"))
    print(test_table.get("hashtable"))


if __name__ == "__main__":
    main()
