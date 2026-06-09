Alpha = ["A","L","P", "H", "A"]
print("List")
for letters in Alpha:
 print (letters);

print("Index")
for i, letters in enumerate(Alpha):
     print(i,letters);

print("Range1")

for i in range(5):
     print(i);

print("Range2")
for i in range(0, 10):
         print(i);

print("Range3")
for i in range(0, 10, 2):
    print(i);

print("While")
y=6
while y<=12:
  print(y)
  y+=1

print("For nested1")
for i in range(4):
    for j in range(i):
        print(i,j)

print("For nested2")
for i in range(4):
   if i == 3:
     break
   for j in range(i):
       if j==2:
           break
print(i, j)

print("For nested3")
for i in range(4):
    if i == 4:
        break
    print(i)
else:
    print("Not in Range")





