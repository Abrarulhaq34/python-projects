# data structure . in this we have 4 types of  in built data structure
# the first one is list
# we can create list by using square brackets

'''a = [ 12,13,14,15,12,16,17.5]
# list is mutable , it has duplicate values, list is ordered, it has heterogenous nature meaning we can store multiple data types inside the list
print(a[0:5]) #slicing
# traversing 
for i in range(len(a)):
    print(a[i])'''
    
#Q print positive and negative numbers of a list

'''l = [12,-34,45,-78,-67,56,-89,87,90]
print("positive numbers are :")
for i in l:
    if i >= 0:
        print(i)    
print("the negative numbers are :")
for i in l:
    if i <= 0:
        print(i)'''
        
#Q mean of a list

'''l = [12,34,23,45,44,34,56]
sum = 0
for i in l:
    sum = sum + i
mean = sum / len(l)
print(mean) '''

#Q findd the greatest element and print its index too

'''l = [12,13,34,45,56,43,25,65,44]

largest = l[0]
index = 0
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
print(f"your largest number is {largest} at index value {index}")  '''



#Q find second largest number

'''l = [12,15,16,17,19,18]

largest = l[0]
sec_largest = l[0]

for i in l :
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(f"your largest number is {largest} and sec_largest number is {sec_largest}") '''


#Q check if list is sorted or not 

'''l = [12,13,14,15,16,17,18] 

for i in range (len(l) -1):
    if l[i] < l[i+1]:
        continue
    else:
        print("your list is not sorted")
        break

else:
    print("your list is sorted") ''' 
    
    
# now lets study the 2nd in build data structure tuple 
# we can create tuple by using paranthesis ()

'''t = (1,2,3,4,5,6,6,6,7.5,"hello")

the tuple is immutable , it can contain duplicate values, it is ordered and it has also heterogenous nature 
# tuple traversing
for i in range(len(t)):
    print(t[i])
    or
        
for i in t:
    print(i)

#tuple unpacking

a,b,c,d = (1,2,3,4) # a will get 1 , b will get 2 and so on ...

# tuple method 
t = (1,2,3,4,4,4,5,6,7)

index = t.index(3)
count = t.count(4)'''
   
# now lets study about the 3rd type sets 
# we can create set by using curved brackets {}

#s = {1,3,5,3,6,9,5}
# the set is mutable , you can not have duplicates , sets are unordered means it can not be accessed by using index value,
# it has semi heterogenous nature it can store some data types string, number, tuple not everything      
        
 #hashing of a string 
 
'''a = hash("hello") 
print(a)  

# lets find the hash value of tuple and set uses the hash value to store the data

b = hash((1,2,3,4,5))
print(b)  

#traversing the set , this is only method and it gives random values.
s = {1,2,8,9,3,4,5,6}
for i in s:
    print(i)  '''           
    
# sets are mutable beacause of set methods...


# now lets study 4th type that is dictionary...
# we can create dictionary by using curly brackets like sets.
# in dictionary there is a pair of keys and values . eg,

# d = {1:"hello", 2:34, 3:"good"} # so there is keys and values...

# dictionary is mutable but the key can not be changed , value can be changed...
# dictionary is duplicated . keys must be unique but values can be duplicated...
# order :- dictionary follows insertion order...
# dictionary has heterogeneous nature . they have multiple data types in it...

'''d = {10:100,20:200,30:300,40:400,50:500}

print(d[10])
print(d[40])   
# we can perform CURD operation on dictionary but we can not change the key after creation          

d[10] = 100 # updating
d[60] = 600 # creating
del d[30]  # deleting 

print(d)'''

# traversing the dictionary. we can both travers key and values.

'''d = {10:100,20:200,30:300,40:400,50:500}

for i in d:
    print(d[i]) # if I print(i) only keys get printed 
    
for i in d.values():
    print(i) '''
    
    
#Q merging two python dictionaries

'''d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]
print(d1)  '''

#Q sum all the values in dictionary

'''d = {10:100,20:200,30:300,40:400,50:500}

sum = 0

for i in d:
    sum = sum + d[i]
print(sum) '''

#Q count the frequency of each element in a list

'''l = [1,1,1,1,2,2,2,3,3,4,4,4,5,5.6,7]
d = {}
for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
        
print(d) '''

#Q combine two dictionaries by adding values for common keys

d1 = {60:100,20:200,40:300}
d2 = {40:400,50:500,60:600}         

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
        
    else:
        d1[i] = d2[i]
        
print(d1)            
                       