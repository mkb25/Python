class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def display(self):
        print(f'Name: {self.name}, Age: {self._age}, Salary: {self.__salary}')

    def get_salary(self):
        return self.__salary
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value


class subEmploy(Employee):
    def show(self):
        print(f'Name: {self.name}, Age: {self._age}')
        # print(f'Salary: {self.__salary}')  # This will raise an Attribute
        print(self.get_salary())  # Accessing salary through a public method
        try:
            print(f'Salary: {self.__salary}')
        except AttributeError as e:
            print("Cannot access private attribute __salary:", e)
    
emp = Employee('Alice', 28, 70000)
emp2 = subEmploy('Bob', 32, 80000)
emp2.show()
emp.display()
print(emp.salary)  # Accessing salary via property
emp2.salary = 75000  # Modifying salary via setter
print(emp2.salary)
print(emp.name)          # Accessible
print(emp._age)     
    # Accessible but discouraged
