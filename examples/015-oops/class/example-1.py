__author__ = 'Gaurav.Khanna'

class Employee:
   'Common base class for all employees'
   emp_count = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.emp_count += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.emp_count)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)

"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee :: %d" % Employee.emp_count)

emp1.displayCount()