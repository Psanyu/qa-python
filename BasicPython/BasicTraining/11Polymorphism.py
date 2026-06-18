#Multi Inheritance
class Cat:
 def __init__(self, s1):
  self.s1 = s1

 def sound(self):
  return "Meow"

# Create the Fox class
class Fox:
  def __init__(self, s1):
    self.s1 = s1

  def sound(self):
    return "Wa-pa-pa-pa-pa-pow!"

c1 = Cat("cat")
f1 = Fox("fox")

print (c1.s1, "makes sound", c1.sound())
print (f1.s1, "makes sound", f1.sound())




