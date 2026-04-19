# if statement

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote")

#     # Enter your age: 40
# You are eligible to vote

#if-else : multiple conditions

# marks = int(input("whats your marks: "))
# if marks >= 90:
#     print("Distinction marks..Excellent")
# elif marks >=60:
#     print("Grade B , You can perform better")
# else:
#     print("Poor performance")

# in this situtation if the candidate puts marks more then 100 then it will give
# distinction but it is not possible ..i should get an error

## nested statements

# marks = int(input("whats your marks: "))
# if marks <= 100 and marks > 0: #if user inputs marks between 0 to 100
#  if marks >= 90:
#         print("Distinction marks..Excellent")
#  elif marks >=60:
#         print("Grade B , You can perform better")
#  else:
#         print("Poor performance")
# else: # if user input negative marks or marks more then 100
#     print ("Are you out of your mind...how can get marks more then 100 or less then zero ")

## Even or odd number:

# num1 = int(input("Enter the number: "))

# if num1 % 2 == 0:
#     print("Even number")
# else:
#     print("Odd")

### Check login access....so pass username and pass from the user (input)...and say if username and pass is same as what user has input then login success otherwise fail

username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "admin123":
    print("login success")
else:
    print("login failed")