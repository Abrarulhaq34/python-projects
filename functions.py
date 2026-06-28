# to create our oun function we use the keyword def 

'''def hello ():
    print("hello wellcome to functions in python")
hello() # calling the function  ''' 
 
# parameters and arguments (1st type positional argumemt)

'''def sum(a , b): # the thing we accept in sum is parameters.and the thing we provide to parameters is arguments
    print(f"the sum of two numbers is {a + b}")
sum (12, 25)
sum (34, 45) #we can call a function infinite times . positional arguments '''

# types of arguments (3 types)
# 2nd type (  keyword argument)

'''def hello (name , age):
    print(f"your name is {name} and your age is {age}")
    
hello (age = 18 , name = "zuhan" )    # i want to print first age and then name that is why we use keyword argument'''

# 3rd type  ( default argument)

'''def greet (name = "guest"):
    print(f"hello,{name}")
greet() # uses default value guest, output is hello guest 
greet("bob")   # uses the value bob ,  output is hello bob'''

#Q check pallindrome

'''def pallindrome (st):
    rev = ""
    for i in range (len(st)-1,-1,-1):
        rev = rev + st[i]
    
    if rev == st:
        print(f"your string  {st} is pallindrome")
    else:
        print(f"your string {st} is not pallindrome")        
    
pallindrome("naman")
pallindrome("elephant") '''

def hello():
    return("hello wellcome to python") #if we use the return then to print the output we must use the print function and also call the function
print (hello())      


