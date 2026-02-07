class Employee:
    def __init__(self,empId = None, name =  None, salary = None):
        self.empId = empId
        self.name = name
        self.salary = salary

    def setEmpId(self,empId):
        self.empId = empId
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary

    def getEmpId(self):
        return self.empId
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
        