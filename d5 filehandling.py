# f = open("file1.csv")
# print(f.read())
# ## show the output of the file

## with keyword

# with open("file1.csv") as f:
#     print(f.read())

## Write to existing file
### we alredy have created a file named akshat.txt with some content 

# newfile = open("akshat.txt", "a") #here a is append 
# newfile.write("\nI hope you are learning something") #\n : new line 
# newfile1 = open("akshat.txt", "r")
# print(newfile1.read())

### Overwrite the existing content:
# newfile = open("akshat.txt", "w")
# newfile.write(''' 
# HEllo welcome to the training
# \nWe all want you to become AI engineer

# ''')
# newfile.close()  ## Here it is important to close the file which is not required in with
# newfile1 = open("akshat.txt", "r")
# print(newfile1.read())

##using with 
with open("akshat.txt", "w" ) as f:
    f.write("oopsi!! we have not closed the file")  #overwrite
with open("akshat.txt") as f:
    print(f.read())