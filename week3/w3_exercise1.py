class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        self.weight += 1
    
    def walk(self):
        if self.weight >= 1:
            self.weight -= 1


def main():
    cat1 = Cat("Binnie", 4, 4)
    cat2 = Cat("Clyde", 1, 2)
    cat3 = Cat("Old Tom", 10, 6)
    cat1.eat()
    cat2.eat()
    cat3.eat()
    print(cat1.weight)
    print(cat2.weight)
    print(cat3.weight)
    cat1.walk()
    cat2.walk()
    cat3.walk()
    print(cat1.weight)
    print(cat2.weight)
    print(cat3.weight)



if __name__ == "__main__":
    main()