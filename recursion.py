# Recursive methods
#GCD:
def gcd(x,y):
   if y==0:
     return x
   else:
       return gcd(y,x%y)
       
print(gcd(60,48))


#Sum of digits:

sum=0
def sum_of_digits(no):
   if no==0:
      return 0
   no2 = int(no//10)
   return no%10 + sum_of_digits(no2)
       
print(sum_of_digits(1234))

# fibonacci series:

def fibo(no):
    if no==1:
       return 1
    elif no==2:
        return 1
    else:
        return fibo(no-1) + fibo(no-2)
       
print(fibo(7))


