class Hashtable:
    def __init__(self, size):
        self.buckets = [[] for i in range(size)]
        self.size = size
    

    def put(self, key, value):
        self.buckets[self.primary_hash(key)].append((key, value))
    
    
    def get(self, key):
        bucket = self.buckets[self.primary_hash(key)]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
            
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
        if test_table.buckets[i] == []:
            continue
        print(f"{i}: {test_table.buckets[i]}")
    
    print(test_table.get("cat"))
    print(test_table.get("act"))
    print(test_table.get("hashtable"))


if __name__ == "__main__":
    main()
