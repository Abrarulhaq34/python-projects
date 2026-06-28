 #while loop is used when we have conditions

# question 1

'''n = int(input("enter the value of n :")) # seperating digites
while n > 0:
    print(n % 10)
    n = n // 10 '''
    
    
# question 2
'''n = int(input("enter the value of n ")) #prints the number in reverse order
rev = 0
while n >0:
    rev = rev * 10 + n % 10
    n = n // 10
    
print(rev) '''       
    
# question 3 check if the digit id pallindromic number ( eg. 121)

'''n = int(input("enter the value of n ")) 
rev = 0
copy = n # we store the copy of n because in last we dont have the original value of n to compere
while n >0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)

if rev == copy:
    print("number is pallindromic")
else:
    print("not the pallindromic number")'''    
    
    
# question 4 python number guessing game using while loop and conditions

import random

num = random.randint(1,100)

tries = 0

while True:
   guess = int(input("please enter your guessing number  between 1 to 100 : "))
 
   if guess == num:
    tries +=1
    print(f"congralutions you guessed the correct number in {tries} tries")
    break

   elif guess > num: 
      print("guess a little bit lower")
      tries +=1
      
   elif guess < num:
      print("guess the little bit higher") 
      tries +=1   
      
   else:
    print("sorry the number you guessed is incorrect") 
    tries +=1                 