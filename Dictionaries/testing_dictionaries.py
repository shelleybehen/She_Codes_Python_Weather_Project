students = ["Angela", "Jen", "Bel"]
#print(students[0])

#Creating a dictionary, separated with comma
#Elements are key:value pairs
#Keys need to be unique, keys can only be immutable
#Immutable data types -> String, Integer, Float, Bool, List
#Calues don't need to be unique, any data type
# Dictionaries are unordered
students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
#print(students_dict)
#print(students_dict.get("Bel"))
#print(students_dict.get("Asli")) #Error
print(students_dict.get("Bel", 0))#get function can take 2 parameters.  2nd parameter is optional. If you can't get Bel, give 0
#Whatever you put as second parameter, means if you can't find the value, give zero.
#Can use a string as well as integer

#print(students_dict["Angela"])
students_dict["Asli"] = 4
#print(students_dict)
students_dict["Jen"] = 10
#print(students_dict)
#delete a key value pair
del students_dict["Asli"]
#print(students_dict)
# print(students_dict.keys()) #all the keys my dict has
# print(students_dict.items()) #tells you all the elements you have in your dictionary and pairs them together
# #Iteration
# for key in students_dict:
#     print(key, students_dict[key]) #returns both the value and key

for key, value in students_dict.items():
    print(key, value)