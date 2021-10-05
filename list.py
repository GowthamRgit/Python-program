#23.09.21 * List programs:*
    
details=[]
name = input("Enter your name")
details.append(name)
hometown = input("Enter your location")
details.append(hometown)
location=input("Enter your location")
details.insert(1,location)
print(details)

marks = [90,89,87.5, 90, 100]
print(len(marks))
for i in range(len(marks)):
    print(marks[i])
    
marks = [90,89,87.5, 90, 100]
marks[0],marks[-1] = marks[-1],marks[0]
print(marks)

#task 1

marks = [90,89,87.5, 90, 100]
sum=0
for mark in marks:
    sum=sum + mark
print(sum)




l1=[10,20,30,10,20,30,10,20,30]
no=10
count=0
for value in l1:
    if value == no:
       count+=1
else:
     print(count)

#28.09.21

name=input('enter your name')
n=name.split()
print (type(n))
for x in n:
    print(x.upper())
    
s1 = 'OYPC'
s2 = 'LMICS'

result=""
i=0
while i<len(s1):
      result = result + s1[i] + s2[i]
      i+=1
else:
    print(result)
    
    
data='a1b2c3'
output = ' '
for i in data:
   if i.isalpha():
       output = output + i
       previous = i
   else:
       output = output + chr(ord(previous)+1) * (int(i) - 1)
else:
     print(output)
         
 # 29.09.21

#list aliasing

import copy
l1 = [10,20,30,40]
print(id(l1))
l2 = copy.copy(l1)
print(id(l2))
l1[0] = 100
print(l1)

 #list cloning
 
l1 = [10,20,30,40]
l2=l1[:]
l2[1]=123
print(l1)
print(l2)


# transposing matrice /  Two dimensional elements

l1 = [ [10,20,30],
       [40,50,60],
       [80,90,100]
     ]
l2=[]
for i in range(len(l1[0])):
   row = []
   for item in l1:
      row.append(item[i])
   l2.append(row)
else:
    print(l2)


