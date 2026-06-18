class op:
    def cars(self):
        models = ["Chev65", "Maruti82", "Kia23"]
        return models

d1 = op()
f = d1.cars()
f.append("Ford99")
print(f)
f.pop(2)
print(f)
f.extend("Tesla")
print(f)
print (f.count("a"))
f.remove("T")
print(f)
f.clear()
print(f)
f.insert(0,"Chev65")
f.insert(1,"Maruti82")
f.insert(2,"Kia23")
print(f)
f.sort()
print(f)
f.reverse()
print(f)
for ch in "Momsc.com":
    if ch == ".":
        break
print(ch, end="")
for i in range(-1,1): print("MyExamCloud", end="")
name ="d"
def d():
    print(name)
    global x
    x=123

d()
print(x)

print("a")
print()
print("b")
print()
print("c")




str = """ """
print(len(str))

