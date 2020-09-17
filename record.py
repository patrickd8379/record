class Record:
    def __init__(self, forename, surname, age, gender, CS_Student, dob):
        self.__forename = forename
        self.__surname = surname
        self.__age = age
        self.__gender = gender
        self.__CS_Student = CS_Student
        self.__dob = dob
        
    def setForename(self, forename):
        self.__forename = forename
        return self.__forename
    def getForename(self):
        return self.__forename
    def setSurname(self, surname):
        self.__surname = surname
        return self.__surname
    def getSurname(self):
        return self.__surname
    def setAge(self, age):
        self.__age = age
        return self.__age
    def getAge(self):
        return self.__age
    def setGender(self, gender):
        self.__gender = gender
        return self.__gender
    def getGender(self):
        return self.__gender
    def setStudent(self, CS_Student):
        self.__CS_Student = CS_Student
        return self.__CS_Student
    def getStudent(self):
        return self.__CS_Student
    def setDob(self, dob):
        self.__dob = dob
        return self.__dob
    def getDob(self):
        return self.__dob
    
    def ageFromDob(self, dob):
        dob = list(dob)
        print(dob)
        dayStr = ""
        monthStr = ""
        yearStr = ""
        day = int(dayStr.join(dob[0][1]))
        month = int(dob[3], dob[4])
        year = int(dob[6], dob[7], dob[8], dob[9])
        print(day, month, year)
    def getBirthdate(self, dob):

        pass
patrick = Record("Patrick", "Debattista", 16, "Male", True, "06/05/2004")
print(patrick.getForename())
print(patrick.ageFromDob(patrick.getDob()))
