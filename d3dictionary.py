student = {
    "name": "Akshat",
    "age": 47
}

# print(student["name"])
# print(student["age"])

#o/p: Akshat
47

# Add new key value
student["college"] = "IIT-Delhi"
# print(student)
#o/p: {'name': 'Akshat', 'age': 47, 'college': 'IIT-Delhi'}

## update the value
## now lets say age is 48...so i want to update age from 47 to 48 
student["age"] = 48
# print(student)
#o/p: 'name': 'Akshat', 'age': 48, 'college': 'IIT-Delhi'}

# Delete the element from the dictionary
## lets say i want to delete the college from the dictionary
del student["college"]
# print(student)
#o/p: {'name': 'Akshat', 'age': 48}

# Nested dictionary

student = {
    "s1": {"name": "Akshat", "age": 47},
    "s2": {"name": "Virat", "age": 35,"sex": "m"}
}
# print(student)
# o/p: {'s1': {'name': 'Akshat', 'age': 47}, 's2': {'name': 'Virat', 'age': 35}}
## lets say in nested dictionary ...change akshat age from 47 to 48

# print(student["s1"]) #o/p: {'name': 'Akshat', 'age': 47}
# print(student["s1"]["age"]) #o/p: 47
# we have reached to age...now we need to chnage age from 47 to 48

student["s1"]["age"] = 48
# print(student["s1"]) #{'name': 'Akshat', 'age': 48}

## Multiple values in the one key

student = {
    "name" : "Akshat",
    "skills": ["devops", "python", "Ai", "Docker"]
}
print(student["skills"]) #['devops', 'python', 'Ai', 'Docker']