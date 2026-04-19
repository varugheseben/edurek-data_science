names = ["akshat", "john","akshat", "aman", "johnson", "adam"] #list
# we have a list of the values 
print(f"list of names is {names}") #here we are printing the names list
#o/p: ['akshat', 'john', 'akshat', 'aman', 'johnson', 'adam']

#now lets convert the list to tuple...tuple is ordered so it will print like 
#in tuples repeatition is allowed
# ('akshat', 'john', 'akshat', 'aman', 'johnson', 'adam')
names_tuple = tuple(names) 
print(f"names in tuple {names_tuple}") #here we are printing tuple list

###
#sets : Unordered unique items
names_set = set(names) #coverting names list to sets 
print(f"names in sets is {names_set} and it is unordered")
#o/p: {'adam', 'john', 'johnson', 'aman', 'akshat'}

##
# list of names is ['akshat', 'john', 'akshat', 'aman', 'johnson', 'adam']
# names in tuple ('akshat', 'john', 'akshat', 'aman', 'johnson', 'adam')
# names in sets is {'adam', 'john', 'johnson', 'aman', 'akshat'} and it is unordered


## Sets :

teama = {"Virat", "Rohit", "Rahul"}
teamb = {"Abhishek", "Surya", "Tilak","Virat"}
#common players between teama and teamb
common = teama & teamb
print(common)
#o/p: {Virat}

# find unique elements (Difference)
# find players only in Teama
only_a = teama - teamb
print(f"players on in teama is {only_a}")

#o/p: players on in teama is {'Rohit', 'Rahul'}

#find players only in teamb
only_b = teamb - teama
print(f"players only in team b is {only_b} ")

#o/p: players only in team b is {'Surya', 'Tilak', 'Abhishek'} 

# union of players in teama and teamb
union_players = teama | teamb
print(f"union of players in {union_players}")
#o/p: union of players in {'Rahul', 'Surya', 'Tilak', 'Virat', 'Abhishek', 'Rohit'}

## methods in sets

##Add an element in sets 
summer_fruits = {"apple", "banana", "pineapple"}
summer_fruits.add("mango")
print(f"After adding mango to fruits : {summer_fruits}") 
# o/p: After adding mango to fruits : {'banana', 'mango', 'pineapple', 'apple'}
# remove fruit :
summer_fruits.remove("banana")
print(f"After removing banana: {summer_fruits}")
# o/p: After removing banana: {'pineapple', 'mango', 'apple'}

# i want to see if a particular fruit is there in the set 
summer_fruits = {"apple", "banana", "pineapple"}
print("banana" in summer_fruits)
# true
print("grapes" in summer_fruits)
#false

### SET is for unique values, not position
# So no replace
# no indexing
#only add and remove the values 

# print(summer_fruits[0])
# # error:
# Traceback (most recent call last):
#   File "/Users/akshat/Desktop/python-scripts/d3sets.py", line 74, in <module>
#     print(summer_fruits[0])
# TypeError: 'set' object is not subscriptable