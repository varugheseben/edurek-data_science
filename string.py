# print("It's a beautiful day!")
# print("he is called 'Johny'")
# print('he is called "johny"')

# a = "Hello"
# print(a)

# b = """hello today is a wonderful day
# we are learning Python
# and we are having fun"""
# print(b)

# c = 'My friends are "Johnny" and \'Tommy\'. '
# print(c)

###

# a = "hello world"
# print(a)
# # print(a[0]) #h
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])
# print(a[8])
# print(a[9])
# print(a[10])

## for loops
# a = "hello world"
# for i in a:
#     print(i)

# a = "hello world"
# print(len(a))

# b = "akshat,lets learn python"
# print(b[:6]) #akshat

# print(b[7:11]) #lets
# print(b[18:24])
# print(b[18:])
# print(b)
# print(b[:])


# matchultiline = """hello world
# I'm robot
# greetings for the day"""
# print(matchultiline[:]) 


#####  python string Method
# text = "hello world"
# # uper_text = text.upper()
# # print(uper_text)
# # # print(text.replace("hello", "hi"))
# # print(uper_text.lower())
# ### python string function
# # text = "hello world"
# # print(len(text))
# # print(max(text))
# print(text.split())

# text = "apple,banana,pineapple,mango,grapes,strawberry"
# print(text.split())

# # o/p ['apple,banana,pineapple,mango,grapes,strawberry']
# print(text.split(",")) #split on the basis of comma
# #o/p: ['apple', 'banana', 'pineapple', 'mango', 'grapes', 'strawberry']


# text = "banana"
# print(text.count("a"))
# # o/p : 3 because we have 3 "a" in banana string

# text = "  python "
# # i want to remove the spaces in the string
# print(text)
# print(text.strip())

# # #o/p:   
# #     python 
# # python

# text = "python programming"
# # i want to change it to like Python programming 
# # print(text)
# # print(text.upper())
# # print(text.capitalize())
# # #o/p:
# # python programming
# # PYTHON PROGRAMMING
# # Python programming
# #I want first letter of each word as capital 
# print(text.title())


# concatenate string 

# a = "Hello"
# b = "World"
# # i want output like "Hello world"
# # c = a + b
# # print(c)
# # o/p: HelloWorld
# # this output is correct but we need space between Hello and World and add welcome
# c = a + " " + b + " " + "Welcome"
# print(c)
# #Hello World Welcome

# text = "hello world"
# # i want hello and world to be printed in different lines

# text = "hello \nWorld"
# print(text)