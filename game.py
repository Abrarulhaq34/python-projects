
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