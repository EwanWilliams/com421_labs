def main():
    
    employees = ["John Stevenson", "Jane Smith", "Tim Wilson", "Kate Stevenson", "Kate Palmer", "Tom Eastman", "Laura Green", "Mike Watson", "Sally Black", "Mark Ramsey"]

    print(employees[1] + " and " + employees[7])
    print()


    searchQuery = input("Search for employee: ")
    searchResult = False

    for i in employees:
        if i == searchQuery:
            searchResult = True
            break
    
    if searchResult == True:
        print(searchQuery + " is an employee")
    else:
        print(searchQuery + " is not an employee")
    



if __name__ == "__main__":
    main()