name ='Sarah'
age = 20

print("1:f-string-op","2:format-op", "3:format-op2", "4:old-style%", sep=(':::::\n'), end='-------\n')

'f string'
print(f'1: Hello my name is {name} and my age is {age}')
'.format'
print('2: Hello my name is {0} and my age is {1}'.format(name, age))
'.format2'
print('3: Hello my name is {} and my age is {}'.format(name, age))
'%'
print('4: Hello my name is %s and my age is %d'%(name, age))



print("1: if-else","2:if-elif-else",sep=('::::::\n'),end='----------\n')

if age < 18:
    print("1: Underage");

if age < 18:
   print("1: Underage")
else:
   print("1: Adult");

if age < 18:
    print("2: Underage")
elif age >= 18 and age < 35:
    print("2: Adult")
elif age >= 35 and age < 60:
    print("2: MiddleAge")
elif age >= 60:
    print("2: Senior")
else:
    print("2: Age not given")



