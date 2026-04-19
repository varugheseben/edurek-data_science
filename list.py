# grocery = ["Biscuits", "bread", "soap", "toothpaste", "butter"]
# print(grocery)
# print(grocery[0])
# print(grocery[1])
# print(grocery[2])
# print(grocery[3])

#list allows duplicate values and allows different datatypes in the string

# fruits = ["banana", "cherry", "cherry", True, 40]
# print(fruits)
# ## length of the list
# #we will use len function
# print(len(fruits))
# print(type(fruits)) #tells what is the datatype of the list

#range of indexes
# fruits = ["banana", "cherry", "pineapple","strawberry"]
# #return third , fourth and fifth item
# print(fruits[2:4])
# # ['pineapple', 'strawberry']
# print(fruits[:2])
# #['banana', 'cherry']
# print(fruits[2:])
# #['pineapple', 'strawberry']

## change the list items

# fruits = ["banana", "cherry", "pineapple","strawberry"]

# print(fruits[1])
# #o/p : cherry
# fruits[1] = "mango" #we are changing the index 1 value of fruits list to mango
# print(fruits)
# print(fruits[1])

# # o/p
# ['banana', 'mango', 'pineapple', 'strawberry']
# mango

# students = ["sreejith", "vinoth"]
# print(students)
# print(students[0])
# print(students[1]) #vinoth

# ## now replacing vinoth with akshat in students list
# students[1] = "akshat"
# print(students[1])
# print(students)

# # o/p: ['sreejith', 'akshat']

# #insert items 
# fruits = ["banana", "cherry", "pineapple","strawberry"]
# # we need to insert watermelon in the fruits list 
# fruits.insert(0, "watermelon")
# print(fruits)
# #o/p: ['watermelon', 'banana', 'cherry', 'pineapple', 'strawberry']

### we need append item in the list 

# cars = ["Rolls-royce Boat tail", "Urus", "Ferrari 812"]
# # i need to append lamborghini in the end of the cars list
# cars.append("lamborghini")
# print(cars)

# o/p: ['Rolls-royce Boat tail', 'Urus', 'Ferrari 812', 'lamborghini']