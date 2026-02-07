class Employee:
    def __init__(self,empId=None,name=None,salary=None):
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


e1 = Employee(1,"emp1",10000)
e2 = Employee()
e2.setEmpId(2)
e2.setName("emp2")
e2.setSalary(20000)

print(e1.getEmpId())
print(e1.getName())
print(e1.getSalary())

print(f"{e2.getEmpId()} {e2.getName()} {e2.getSalary()}")