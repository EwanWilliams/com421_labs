class Student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course
        self.mark = 0
    
    def __str__(self):
        return f"{self.name} | ID: {self.id} | Course: {self.course} | Mark: {self.mark}"
    
    def setMark(self, markInput):
        if markInput >= 0 and markInput <= 100:
            self.mark = markInput
            return True
        else:
            return False
    
    def getGrade(self):
        if self.mark >= 70:
            return "First"
        elif self.mark >= 60 and self.mark <= 69:
            return "2/1"
        elif self.mark >= 50 and self.mark <= 59:
            return "2/2"
        elif self.mark >= 40 and self.mark <= 49:
            return "Third"
        elif self.mark >= 0 and self.mark <= 39:
            return "Fail"
    
    def didPass(self):
        if self.mark >= 40:
            return True
        else:
            return False
    


def main():
    #init empty array
    studentBody = [None] * 5
    #for number of students to add
    for i in range(5):
        markValid = False
        #take basic student details to init object
        newStudent = Student(i, input(f"Enter student {i+1} name: "), input(f"Enter student {i+1} course: "))
        #use setMark() method to only store mark if valid
        while markValid == False:
            markValid = newStudent.setMark(int(input(f"Enter student {i+1} mark: ")))
            if markValid == False: print("ERROR INVALID MARK")
        
        studentBody[i] = newStudent #store student object to array
    
    #loop through every item in the array
    for pupil in studentBody:
        print(pupil, end=" | ") #print stored data
        print(pupil.getGrade(), end=" | ") #print grade using getGrade() method
        print(f"Pass? {pupil.didPass()}") #print pass/fail status using didPass() method



if __name__ == "__main__":
    main()