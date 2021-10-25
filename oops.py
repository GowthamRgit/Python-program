class School:
      '''State Board Scchool - Govt. of Tamil Nadu'''
print(School.__doc__)
help(School)

class School:
      '''State Board Scchool - Govt. of Tamil Nadu'''
  
  #constructor--  Intializing object specfic variables  
      def __init__(self,name,age,qual,exp):
          self.t_name = name
          self.t_age = age
          self.t_qual = qual
          self.t_exp = exp
          
      def inspect(self):    
          print(self.t_name)
          print(self.salary)
      
      def pay(self,salary): #salary -- local variable
          #print(salary)
          self.salary = salary
          
 
teacher1 = School("Raghu", 25, "M.Sc.", 13) #object specfic values
teacher2 = School("Ram", 35, "M.Sc. M.Phill", 13) 
teacher1.pay(10000)
teacher2.pay(20000)
teacher1.inspect() #function calling
teacher2.inspect()


class School:
      '''State Board Scchool - Govt. of Tamil Nadu'''
  
  #constructor--  Intializing object specfic variables  
      def __init__(self, *details):    #variable length arguments (constructor overloading)
          for info in range(len(details)):
	      self.t_name = details[0]   #instance variable
              self.t_age = details[1]
              self.t_qual = details[2]
              self.t_exp = details[3]
            
      def inspect(self):    
          print(self.t_name)
          print(self.salary)
      
      def pay(self,salary): #salary -- local variable
          #print(salary)
          self.salary = salary   #instance variable
          
 
teacher1 = School("Raghu", 25, "M.Sc.", 13) #object specfic values
teacher2 = School("Ram", 35, "M.Sc. M.Phill", 13) 
teacher3 = School("Rajesh", 45, "M.Sc. M.Phill") 
teacher1.pay(10000)
teacher2.pay(20000)
teacher1.inspect() #function calling
teacher2.inspect()
teacher3.pay(32000)
teacher3.inspect()

class Employee:

     def __init__(self,eNo,eName):
         self.eID= eNo
         self.name = eName

e1 = Employee(123 ,"BCD")
print(e1.__dict__)


class School:
      '''State Board Scchool - Govt. of Tamil Nadu'''
  
  #constructor--  Intializing object specfic variables  
      def __init__(self, *details):    #variable length arguments (constructor overloading)
          for info in range(len(details)):
	      self.t_name = details[0]   #instance variable
              self.t_age = details[1]
              self.t_qual = details[2]
              self.t_exp = details[3]
            
      def inspect(self):    
          print(self.t_name)
          print(self.salary)
      
      def pay(self,salary): #salary -- local variable
          #print(salary)
          self.salary = salary   #instance variable
          
 
teacher1 = School("Raghu", 25, "M.Sc.", 13) #object specfic values
teacher2 = School("Ram", 35, "M.Sc. M.Phill", 13) 
teacher3 = School("Rajesh", 45, "M.Sc. M.Phill") 

teacher1.pay(10000)
teacher2.pay(20000)
teacher1.inspect() #function calling/method calling statement
teacher2.inspect()
teacher3.pay(32000)
teacher3.inspect()
teacher3.promotion = True  #outside class 
print(teacher.__dict__)
del teacher3.t_qual
print(teacher3.__dict__)
