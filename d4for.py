food = ["burger", "pizza", "momos", "noodles"]

# print(food[0])
# print(food[1])
# print(food[2])

# for i in food: 
#     print(f"Here is the {i}")

#o/p:
# Here is the burger
# Here is the pizza
# Here is the momos
# Here is the noodles
# for i in range(10):
#     print(i)

#o/p: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# food = ["burger", "pizza", "momos", "noodles"]
# elements_list = len(food)
# print(elements_list)
# # print(food[0])
# for i in food: #for every element in list food
#     # i = burger
#     #i = pizza
#     # i = momos
#     #i = noodles 
#     print(f"Here is the {i}")
# #method 2
# for i in range(elements_list):  #for every element in range(4) i -0 i -1 i-2 i-3
#     print(food[i])


# ## lets say i want to only print second and third value
# for i in range(1,3):
#     print(f"Here is two food i like: {food[i]}")
# #     o/p: Here is two food i like: pizza
# # Here is two food i like: momos


# SUPPOSE WE ARE DEALING WITH THE STRING

name = str(input("What is your name: "))
# we need to print that string
#without loops
# print(name[0])
# print(name[1])
# print(name[2])
length_name = len(name)
print(length_name)

## method 1 (with loops using range)
# for i in range(0,length_name):
    #i will be in range 0 to 6 where first i =0 i =1 i =2 i=3 i=4 and so on
    # print(name[i])
# #o/p: j
# o
# h
# n

## method2
# for i in name:  #for every element in the name 
#     print(i)

# # j
# o
# h
# n