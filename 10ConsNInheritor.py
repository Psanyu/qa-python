from grpc import CallCredentials


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

class Dog:
 def __init__ (self, name, age):
    self.name = name
    self.age = age

 def bark(self) :
    return "says Woof!"

# Create an object
d1 = Dog("Buddy", 3 )

# Call the bark method

print (d1.name, "of age" , d1.age, d1.bark())


class Person:
  lastname = "Jackson"

  def __init__(self, name):
    self.name = name

p1 = Person("Emil")
p2 = Person("Tobias")
Person.lastname = "Hansen"
print(p1.lastname)

class Calc:
 def __init__(self, a, b):
        self.a = a
        self.b = b

 def add(self):
    return self.a + self.b

 def sub(self):
    return self.a - self.b

c1 = Calc(2,3)
c2 = Calc(8,5)

print(c1.add())
print(c2.sub())







