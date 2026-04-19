# daysoftheweeks = ("sunday", "monday", "tuesday", "wednesday", "thusday", "friday", "saturday")
# # print(daysoftheweeks)

# # #o/p: ('sunday', 'monday', 'tuesday', 'wednesday', 'thusday', 'friday', 'saturday')

# # print(daysoftheweeks[1]) #o/p: monday
# # print(daysoftheweeks[2])

# # # lets try changing the values. - WE CANNOT DO IT IN TUPLE
# # daysoftheweeks[1] = "mon"
# # print(daysoftheweeks)

# # #o/p: Traceback (most recent call last):
# # #   File "/Users/akshat/Desktop/python-scripts/tuple.py", line 10, in <module>
# # #     daysoftheweeks[1] = "mon"
# # # TypeError: 'tuple' object does not support item assignment

# # see the type of the tuple

# print(type(daysoftheweeks))
# # <class 'tuple'>


# But suppose i have to change the tuple value 

# tuple ---> change to list --> change the value --> change the list to tuple
x = ("apple", "kiwi", "banana","orange")
#change kiwi to melon ...but we know we cannot change the tuple values
y = list(x) #we are creating a new variable y which is the list of tuple x
print(f"converted the tuple to list {y} with type: {type(y)}")
#['apple', 'kiwi', 'banana', 'orange']
y[1] = "melon"
print(f"after changing the value of kiwi to melon : {y} with {type(y)}")
# converted the tuple to list ['apple', 'kiwi', 'banana', 'orange'] with type: <class 'list'>
# after changing the value of kiwi to melon : ['apple', 'melon', 'banana', 'orange'] with <class 'list'>

# now lets convert list to tuple
x = tuple(y)
print(f"we have now change back to tuple: {x} with type as: {type(x)}")

# we have now change back to tuple: ('apple', 'melon', 'banana', 'orange') with type as: <class 'tuple'>