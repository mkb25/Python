class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

person = Person('John Doe', 30) 
print(person)
for attr in person.__dict__: 
    #f not attr.startswith('__'): 
    print(attr)
 
print(getattr(person, 'name')) # John Doe 
print(getattr(person, 'age')) # 30 
print(getattr(person, 'city', 'Milano')) # Milano
print(person.__dict__)
setattr(person, 'age', 31)
setattr(person, 'city', 'New York')
print(person.__dict__)
