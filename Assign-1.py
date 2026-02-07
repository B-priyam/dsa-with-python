class Employee:
    def __init__(self,empId,name,salary):
        self.empId = empId
        self.name = name
        self.salary = salary

    def getEmpDetails(self):
        print("id",self.empId)
        print("name",self.name)
        print("salary",self.salary)


