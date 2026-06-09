class Person:
    def __init__(self, name, age):
        self.name = name        # store as instance variable
        self.age = age

    def greet(self):            # method at class level, needs self
        print("Hello, my name is", self.name)

p1 = Person("John", 36)
p1.greet()                      # Hello, my name is John
print(p1.name)                  # John
print(p1.age)
