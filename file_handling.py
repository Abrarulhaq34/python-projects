# # lets study about file handling in python
file = open('geek.txt','r')
print(file)
file.close()
print("file name: ", file.name)
print("file mode: ", file.mode)
print("is closed:", file.closed)

# now we will write a content in a file 
with open('geek.txt','w') as file:
    file.write("welcome to the world of programming\n")
    file.write("python is a easy and powerful programming language to learn")
    
print("content written to the file successfully")
file = open("geek.txt","r")
content = file.read()
print(content)
file.close()
