# # Demonstrate a function

# def create_greeting(name):
#     greeting = f"Hello, {name}!"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Ivy"))
# print(create_greeting("Remus"))

# #Create a function that takes an integer as a parameter and returns that integer multiplied by 3

# def calculation(x): #what we called the function
#     multiply = x * 3 #what it does
#     return multiply

# print(calculation(10)) #how to call the function

def convert_cm_to_in(length_cm):
    length_in_inch = length_cm / 2.54
    return length_in_inch

# print(convert_cm_to_in(20))

# print(length_in_inch) #is not defined because it is a local variable

#write a function that converts inches to cm

# def convert_in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm

# print(convert_in_to_cm(20))

# def add(a,b):
#     #result = a + b
#     #return result
#     #return a + b

#     print(add(2,3))

def calculate_mean(a, b):
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(3,4))