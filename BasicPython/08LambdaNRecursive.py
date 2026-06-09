def factorial(n):
    if n == 1:              # stop condition
        return 1
    return n * factorial(n - 1)   # calls itself

print (factorial(5))

def sub(Sz):
    if Sz == 4:              # stop condition
        return 1
    return Sz * sub(Sz - 1)   # calls itself

print (sub(4))

def sub(Sz):
    if Sz <= 1:        # safer stop condition
        return 1
    return Sz * sub(Sz - 1)

print (sub(3))

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)


  def simple_gen():
      yield "Emil"
      yield "Tobias"
      yield "Linus"


  gen = simple_gen()
  print(next(gen))
  print(next(gen))
  print(next(gen))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
y=len(mytuple)
for i in range(y):
    print(next(myit))



