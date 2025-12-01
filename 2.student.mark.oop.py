class Student:
    def __init__(self, id, name, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_dob(self, dob):
        self.__dob = dob
    
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
    
    def set_cId(self, cId):
        self.__cId = cId
    
    def set_cName(self, cName):
        self.__cName = cName

    def get_cId(self):
        return self.__cId
    
    def get_cName(self):
        return self.__cName
    
    def __str__(self):
        return f"Course id: {self.get_cId()}, name: {self.get_cName()}"

class Mark(Student, Course):
    def __init__(self, id, name, cName, mark):
        super().__init__(self, id, name)
        self.set_cName(cName)
        self.__mark = mark
    
    def get_mark(self):
        return self.__mark
    
    def __str__(self):
        return f"Student name: {self.get_name()}, course : {self.get_cName()}, mark: {self.get_mark()}"

def main():
    tinh = Student("23BA14283", "Tinh", "29/04/2005")
    oop = Course("ICT001", "Oop")
    m1 = Mark(tinh.get_id(),tinh.get_name(), oop.get_cName(), 10.00)
    print(oop)
    print(tinh)
    print(m1)
main()
    