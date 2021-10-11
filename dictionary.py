# 05.10.21  Dictionary Programs

d = {}
d = dict()
d['Tamil 1'] = '9 am'
d['Tamil 2'] = '9 am'
print(d)
print(d['Tamil 1'])

marks = {}
choice = ""
while choice != 'ok':
      subname = input(" Enter subject name")
      mark = int(input(" Enter mark"))
      marks[subname] = mark
      choice = input("Shall I stop getting marks?")
else:
     print(marks)	
     for sub in marks:
        print(sub, "\t", marks[sub])

marks['tamil'] = 55
marks['hindi'] = 65
print(marks)

del d['hindi']
marks.clear()
print(marks)

del marks
print(marks)


# Dictionary fuctions

d = dict([(1, 'kathir'), (2, 'kavin'), (3, 'vijayan')])
print(d)
print(len(d))
print(d.keys())
print(type(d.keys()))
print(d.values())
print(type(d.values()))
print(d.items())
print(type(d.items()))

	        

d = dict([(1, 'kathir'), (2, 'kavin'), (3, 'vijayan')])

d.setdefault(1, 'arul')
d.setdefault(4, 'arul')

print(d)

d2 = d.copy()

print(d2)
     
#no of occurences of each character
name = 'shivashankar'
d = {}
print(d.get('s'))
print(d.get('s',0))

for letter in name:
    d[letter] = d.get(letter,0)+1
    print(letter, '-->',d[letter])
else:
    print(d)
    
    
#no occurrencs of vowels in given string

name = 'vinothkumar mukesh gowtham'

d = {}
vowels = {'a','e','i','o','u'}
for letter in name:   
   if letter in vowels:
      d[letter] = d.get(letter, 0)+1
else:
     for k,v in sorted(d.items()):
         print(k, '-->', v)            	

#add marks in all subjects

marks = {'first':45, 'second':67, 'third':58}
for key, value in marks.items():
    marks[key] = value + 2
else:
     print(marks)
     
     
#add salary of all employees

employees = {'ab':12000, 'bc':10000, 'de':15000, 'ef':13000}
total = 0
for key, value in employees.items():
    total = total + value 
else:
     print(total)
     
     
#how many employees above 12000

employees = {'ab':12000, 'bc':10000, 'de':15000, 'ef':13000}
total = 0
for key, value in employees.items():
    if value >= 12000:
       print(key)
       
#students marks adding

students = {'raja':[56,45,67], 'raju':[78,89,90]}
print(students)
total = 0
for key, value in students.items():
    for values in value:
        total = total + values
    print(key,' --> ',total)



