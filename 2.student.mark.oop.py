lsStudent = []
lsCourse = []
lsMark = []
class Student:
    def __init__(self, id, name, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
# setter
    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_dob(self, dob):
        self.__dob = dob
# getter
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    
    def __str__(self):
        return f"Student id: {self.get_id()}, name: {self.get_name()}, Dob: {self.get_dob()}"

class Course:
    def __init__(self, cId, cName):
        self.__cId = cId
        self.__cName = cName
# setter
    def set_cId(self, cId):
        self.__cId = cId
    def set_cName(self, cName):
        self.__cName = cName
# getter
    def get_cId(self):
        return self.__cId
    def get_cName(self):
        return self.__cName
    
    def __str__(self):
        return f"Course id: {self.get_cId()}, name: {self.get_cName()}"

class Mark():
    def __init__(self, sId, cId, mark):
        self.__sId = sId
        self.__cId = cId
        self.__mark = mark

    def get_mark(self):
        return self.__mark
    def get_sId(self):
        return self.__sId
    def get_cId(self):
        return self.__cId
    
    def __str__(self):
        return f"Student ID: {self.get_sId()}, course ID: {self.get_cId()}, mark: {self.get_mark()}"
    

def inputStudent():
    n = int(input("Enter number of students: "))
    for i in range (n):
        print(f"------Student #{i+1}------")
        id = input(f"Student #{i+1} ID: ")
        name = input(f"Student #{i+1} Name: ")
        dob = input(f"Date of birth: ")
        lsStudent.append(Student(id, name, dob))

def inputCourse():
    n = int(input("Enter number of courses: "))
    for i in range (n):
        print(f"------Course #{i+1}------")
        id = input(f"Course #{i+1} ID: ")
        name = input(f"Course #{i+1} Name: ")
        lsCourse.append(Course(id, name))

def listCourse():
    print("------List of Courses------")
    for i in range (len(lsCourse)):
        print(lsCourse[i])

def listStudent():
    print("------List of Students------")
    for i in range (len(lsStudent)):
        print(lsStudent[i])

def inputMark():
    cId = input("Enter course id to input mark: ")
    check = False
    for c in lsCourse:
        if cId == c.get_cId():
            check = True
            break
    if check == True:
        sId = input("Enter student id: ")
        mark = float(input("Enter mark: "))
        lsMark.append(Mark(sId, cId, mark))
    else:
        return

def listMark():
    check = False
    cId = input("Enter course id to show mark: ")
    print(f"------Marks for course {cId}------")
    for m in lsMark:
        if cId == m.get_cId():
            check = True
            sName = ""
            for s in lsStudent:
                if m.get_sId() == s.get_id():
                    sName = s.get_name()
                    break
            if(sName != ""):
                print(f"Student ID: {m.get_sId()}, name: {sName}, mark: {m.get_mark()}")
    if not check:
        print("This course doesnt have mark yet!")
def main():
    inputStudent()
    inputCourse()
    listStudent()
    listCourse()
    inputMark()
    listMark()
main()
    