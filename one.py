
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



     
     
     
