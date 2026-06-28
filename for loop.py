# lets study about for loops
#for i in range (1,11,1):
 #   print(i)
# so in the range function it is the start value , stop value and the step value

#so lets print any table 

'''n = int (input("enter the number "))
for i in range (n , n*10+1 , n ) :
    print(i)'''
    
## lets see the loops in  string

'''a = " my name is abrar"
 #len(a) give the actual  length of string
for i in range(len(a)):
    print(a[i])'''
  
# now break and continue statement

'''for i in range( 15):
    if i == 10:
        break  # it will terminate at the value 10
    print(i) '''
    
'''for i in range(20):
    if i == 12:
        continue # basically it will skip the 12 value     
    print(i)'''
    
    
#1 for loop questions practice

'''n = int(input("enter the number : "))
for i in range(n):
    print("hello world")  '''
    
    
#2 2nd question

'''n = int(input("enter the number : "))
print("the natural numbers are : ")
for i in range(1,n):
    print(i) '''     
     
# printing of table

'''n = int(input("enter the number n "))
for i in range(1,11):
    print(f"{n} * {i} = {n * i}") '''
    
        
#3 3rd question
'''n = int(input("tell me the value of n : "))
print("the numbers from n to 1 are : ")
for i in range(n ,0,-1):
    print(i)'''
    
#4 4th question

'''n = int(input("enter the value of n : ")) 
print("the sum of n numbers is : ")
sum = 0
for i in range(n+1):
    sum = sum + i
print(sum) '''

#5 5th question

'''n = int(input("enter the value of n : "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print("the factorial of a number is :",factorial ) '''

#6  6th question

'''n = int(input("enter the value of n : "))
sum = 0
for i in range(2,n+1 ,2):
    sum = sum + i
print("the sum of even numbers are : ", sum)  '''

#7 7th question

'''n = int(input("enter the value of n : ")) 
sum = 0
for i in range(3 , n+1 ,2):
    sum = sum + i 
print("the sum of odd numbers are ", sum) '''

#8 8th question

'''n = int(input("enter the value of n : "))
print("the factors of a number are : ")
for i in range(i,n+1):
    if n % i ==0:
        print(i)'''
     
#9 9th question

'''n = int(input("enter the value of n : "))
sum = 0
for i in range(1,n):
    if n % i == 0:
     sum = sum + i 
if sum == n:     
     print("the given number is perfect number")
else:
    print("it is not PN ") '''
    
#10 10th question

'''n = int(input("enter the value of n  "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("the number is prime ")
else:
    print("the number is composit") '''
    
#11 11th question reverse of a string

'''a = "abrarulhaq"               
for i in range(len(a)-1,-1,-1):
    print(a[i]) '''         

# P a l l i n d r o m e  = a word if we read it also in reverse order        


#12 12th question

a = " P @ # y n 2 6 a t ^ & i 5 v e "
dig = 0
char = 0
spchar = 0

for i in a:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(dig,char,spchar)                