from pickle import GLOBAL

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

def myfunc2(x, *y):
    a = y[0]      # 1
    b = y[1]      # 4
    c = a + b + x
    return c

print("Args", myfunc2(10, 1, 4))

x = 0  # global variable

def myfunc3(**y):
    global x
    x = "children"
    y[0] = {"name": "Sarah", "age": 5}
    y[1] = {"name": "Sam", "age": 10}
    return x, y


def s():
    def t2():
        return 5
    t3 = t2() + 5
    return t3

print("Decorators", s())


def n():
    def s1():
        return 5

    def s3():
        return 5

    z = s1() + 5
    z1 = s3() ** 2 + 5
    return z, z1

print("Multiple Decorators", n())

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))
print(result)

result = list(filter(lambda x:x%2==0 ,numbers))
print(result)

students = [
    {"name": "Sam", "age": 10},
    {"name": "Sarah", "age": 5},
    {"name": "Tom", "age": 8}
]

# sort by age
sorted_students = sorted(students, key=lambda x: x["age"])
print(sorted_students)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
