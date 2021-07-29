# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08,
#     }

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
#     }

# for key in groceries:
#     calculation = round(groceries[key] * quantity[key], 2)
# #     print(f"{quantity[key]} {key} @ ${groceries[key]} = ${calculation}")
# #Dictionary
# colour_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0
#     }

# #List
# colours = [
#     "orange",
#     "purple",
#     "blue",
#     "yellow",
#     "green",
#     "green",
#     "purple",
#     "purple",
#     "green",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "blue",
#     "green",
#     "orange",
#     "orange",
#     "red",
#     "yellow",
#     "yellow"
# ]

# for item in colours:  #iterating over a list
#     colour_counts[item] +=1 #every time loops through, adds 1 to the colour_counts dictionary
# for key, value in colour_counts.items(): #accessing the dict of colour counts using the name of the colour. Changing the value of that partic colour.
#     print(f"{key}: {value}")

names = [
    "Maddy",
    "Bel", 
    "Elnaz", 
    "Gia", 
    "Izzy",
    "Joy", 
    "Katie", 
    "Maddie", 
    "Tash", 
    "Nic",
    "Rachael", 
    "Bec", 
    "Bec", 
    "Tabitha", 
    "Teagen",
    "Viv", 
    "Anna", 
    "Catherine", 
    "Catherine", 
    "Debby",
    "Gab", 
    "Megan", 
    "Michelle", 
    "Nic", 
    "Roxy",
    "Samara", 
    "Sasha", 
    "Sophie", 
    "Teagen", 
    "Viv"
    ]

unique_names = dict.fromkeys(names, 0)
print(unique_names)
dictionary = unique_names
for item in names:
    dictionary[item] +=1
for key, value in dictionary.items():
    print(f"{key} : {value}")